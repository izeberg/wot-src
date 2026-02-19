package net.wg.story_mode.battle.views.intro
{
   import fl.transitions.easing.Strong;
   import flash.display.MovieClip;
   import flash.events.FocusEvent;
   import net.wg.gui.components.common.video.PlayerStatus;
   import net.wg.gui.components.common.video.SimpleVideoPlayer;
   import net.wg.gui.components.common.video.VideoPlayerEvent;
   import net.wg.gui.components.common.video.VideoPlayerStatusEvent;
   import net.wg.gui.components.common.waiting.WaitingMc;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.events.UILoaderEvent;
   import net.wg.infrastructure.events.StageSizeMangerEvent;
   import net.wg.story_mode.battle.views.intro.data.IntroVideoVO;
   import net.wg.story_mode.infrastructure.base.meta.IIntroVideoMeta;
   import net.wg.story_mode.infrastructure.base.meta.impl.IntroVideoMeta;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   import scaleform.clik.motion.Tween;
   import scaleform.gfx.FocusManager;
   
   public class IntroVideo extends IntroVideoMeta implements IIntroVideoMeta
   {
      
      private static const STAGE_RESIZED:String = "stageResized";
      
      private static const BREAK_POINT:String = "breakPoint";
      
      private static const SUBTITLE_CHANGE:String = "subtitleChange";
      
      private static const BTN_SKIP_OFFSET_Y:int = -88;
      
      private static const BUFFERING_TIME:Number = 0.5;
      
      private static const SUBTITLE_OFFSET:int = 100;
      
      private static const TWEEN_DURATION:int = 500;
      
      private static const VIDEO_ERROR:String = "IntroVideo error: ";
      
      private static const BACKGROUND_WIDTH:Number = 2560;
      
      private static const BACKGROUND_HEIGHT:Number = 1440;
      
      private static const BACKGROUND_ASPECT_RATIO:Number = BACKGROUND_WIDTH / BACKGROUND_HEIGHT;
       
      
      public var blackBG:MovieClip = null;
      
      public var videoPlayer:SimpleVideoPlayer = null;
      
      public var btnSkipVideo:SoundButtonEx = null;
      
      public var waiting:WaitingMc;
      
      public var subtitle:IntroVideoSubtitle = null;
      
      public var loadingImage:UILoaderAlt = null;
      
      private var _data:IntroVideoVO = null;
      
      private var _subtitleText:String = null;
      
      private var _isPaused:Boolean = false;
      
      private var _isLoaded:Boolean = false;
      
      private var _videoCompleted:Boolean = false;
      
      private var _playerOriginalWidth:Number;
      
      private var _playerOriginalHeight:Number;
      
      private var _playerOriginalScaleX:Number;
      
      private var _playerOriginalScaleY:Number;
      
      private var _tweenFadeOut:Tween = null;
      
      public function IntroVideo()
      {
         super();
         focusable = true;
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         invalidate(STAGE_RESIZED);
      }
      
      override protected function setData(param1:IntroVideoVO) : void
      {
         this._data = param1;
         invalidateData();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         App.stageSizeMgr.addEventListener(StageSizeMangerEvent.BREAK_POINT_CHANGED,this.onBreakPointChangedHandler);
         this.videoPlayer.addEventListener(VideoPlayerEvent.PLAYBACK_STOPPED,this.onVideoPlayerPlaybackStoppedHandler,false,0,true);
         this.videoPlayer.addEventListener(VideoPlayerStatusEvent.ERROR,this.onVideoPlayerErrorHandler,false,0,true);
         this.videoPlayer.addEventListener(VideoPlayerStatusEvent.STATUS_CHANGED,this.onVideoPlayerStatusChangedHandler,false,0,true);
         this.videoPlayer.bufferTime = BUFFERING_TIME;
         this._playerOriginalWidth = this.videoPlayer.width;
         this._playerOriginalHeight = this.videoPlayer.height;
         this._playerOriginalScaleX = this.videoPlayer.scaleX;
         this._playerOriginalScaleY = this.videoPlayer.scaleY;
         this.btnSkipVideo.addEventListener(ButtonEvent.CLICK,this.onSkipVideoButtonClickHandler);
         this.btnSkipVideo.visible = false;
         this.loadingImage.addEventListener(UILoaderEvent.COMPLETE,this.onBackgroundCompleteHandler,false,0,true);
      }
      
      private function onBackgroundCompleteHandler(param1:UILoaderEvent) : void
      {
         this.setBackgroundSize();
      }
      
      private function setBackgroundSize() : void
      {
         var _loc1_:int = App.appWidth;
         var _loc2_:int = App.appHeight;
         var _loc3_:Number = _loc2_ * BACKGROUND_ASPECT_RATIO;
         if(_loc3_ < _loc1_)
         {
            this.loadingImage.width = _loc1_;
            this.loadingImage.height = _loc1_ / BACKGROUND_ASPECT_RATIO;
            this.loadingImage.y = _loc2_ - this.loadingImage.height >> 1;
         }
         else
         {
            this.loadingImage.width = _loc3_;
            this.loadingImage.height = _loc2_;
            this.loadingImage.x = _loc1_ - this.loadingImage.width >> 1;
         }
      }
      
      protected function tweenFadeOut() : void
      {
         this._tweenFadeOut = new Tween(TWEEN_DURATION,this.loadingImage,{"alpha":0},{"ease":Strong.easeIn});
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA) && this._data)
         {
            this.loadingImage.source = this._data.loadingImage;
            this.btnSkipVideo.label = this._data.skipButtonLabel;
            this.waiting.setMessage(this._data.loadingText);
            this._isPaused = this._data.isPausedAfterLoad;
            invalidate(STAGE_RESIZED);
         }
         if(isInvalid(SUBTITLE_CHANGE))
         {
            this.subtitle.update(this._subtitleText);
         }
         if(isInvalid(STAGE_RESIZED))
         {
            this.updateUIPosition();
         }
         if(isInvalid(BREAK_POINT))
         {
            this.subtitle.updateBreakPoint();
         }
      }
      
      override protected function onDispose() : void
      {
         this.disposePlayer();
         App.utils.scheduler.cancelTask(this.showSkip);
         App.stageSizeMgr.removeEventListener(StageSizeMangerEvent.BREAK_POINT_CHANGED,this.onBreakPointChangedHandler);
         this.btnSkipVideo.removeEventListener(ButtonEvent.CLICK,this.onSkipVideoButtonClickHandler);
         this.btnSkipVideo.removeEventListener(FocusEvent.FOCUS_OUT,this.onBtnFocusOutHandler);
         this.loadingImage.removeEventListener(UILoaderEvent.COMPLETE,this.onBackgroundCompleteHandler);
         this.blackBG = null;
         this.btnSkipVideo.dispose();
         this.btnSkipVideo = null;
         this.waiting.dispose();
         this.waiting = null;
         this.subtitle.dispose();
         this.subtitle = null;
         this.loadingImage.dispose();
         this.loadingImage = null;
         if(this._tweenFadeOut != null)
         {
            this._tweenFadeOut.dispose();
            this._tweenFadeOut = null;
         }
         super.onDispose();
      }
      
      public function as_loaded() : void
      {
         this.waiting.visible = false;
         this.tweenFadeOut();
         this._isLoaded = true;
         if(this._data && !this._isPaused)
         {
            this.videoPlayer.source = this._data.video;
         }
      }
      
      public function as_pausePlayback() : void
      {
         this._isPaused = true;
         if(this._isLoaded)
         {
            this.videoPlayer.pausePlayback();
         }
      }
      
      public function as_resumePlayback() : void
      {
         this._isPaused = false;
         if(this._isLoaded)
         {
            if(StringUtils.isEmpty(this.videoPlayer.source))
            {
               this.videoPlayer.source = this._data.video;
            }
            else
            {
               this.videoPlayer.resumePlayback();
            }
         }
      }
      
      protected function disposePlayer() : void
      {
         if(this.videoPlayer)
         {
            this.videoPlayer.removeEventListener(VideoPlayerStatusEvent.STATUS_CHANGED,this.onVideoPlayerStatusChangedHandler);
            this.videoPlayer.removeEventListener(VideoPlayerEvent.PLAYBACK_STOPPED,this.onVideoPlayerPlaybackStoppedHandler);
            this.videoPlayer.removeEventListener(VideoPlayerStatusEvent.ERROR,this.onVideoPlayerErrorHandler);
            this.videoPlayer.dispose();
            this.videoPlayer = null;
         }
      }
      
      private function showSkip() : void
      {
         this.btnSkipVideo.visible = true;
         FocusManager.setFocus(this.btnSkipVideo);
         this.btnSkipVideo.addEventListener(FocusEvent.FOCUS_OUT,this.onBtnFocusOutHandler);
         onSkipButtonVisibleS();
      }
      
      private function onSkip() : void
      {
         this.btnSkipVideo.visible = false;
         this.completeVideo(true);
      }
      
      private function updateUIPosition() : void
      {
         var _loc3_:Number = NaN;
         var _loc1_:int = App.appWidth;
         var _loc2_:int = App.appHeight;
         this.blackBG.width = _loc1_;
         this.blackBG.height = _loc2_;
         if(_loc1_ / _loc2_ > this._playerOriginalWidth / this._playerOriginalHeight)
         {
            _loc3_ = _loc1_ / this._playerOriginalWidth;
            this.videoPlayer.scaleX = this._playerOriginalScaleX * _loc3_;
            this.videoPlayer.scaleY = this._playerOriginalScaleY * _loc3_;
         }
         else
         {
            _loc3_ = _loc2_ / this._playerOriginalHeight;
            this.videoPlayer.scaleX = this._playerOriginalScaleX * _loc3_;
            this.videoPlayer.scaleY = this._playerOriginalScaleY * _loc3_;
         }
         this.videoPlayer.x = _loc1_ - this.videoPlayer.width >> 1;
         this.videoPlayer.y = _loc2_ - this.videoPlayer.height >> 1;
         this.btnSkipVideo.x = _loc1_ - this.btnSkipVideo.width >> 1;
         this.btnSkipVideo.y = _loc2_ + BTN_SKIP_OFFSET_Y;
         if(this.waiting.visible)
         {
            this.waiting.x = _loc1_ - this.waiting.width >> 1;
            this.waiting.y = _loc2_ - this.waiting.height >> 1;
         }
         this.subtitle.x = _loc1_ >> 1;
         this.subtitle.y = _loc2_ - SUBTITLE_OFFSET;
         this.subtitle.updateSize();
         this.setBackgroundSize();
      }
      
      private function completeVideo(param1:Boolean = false) : void
      {
         if(this._videoCompleted)
         {
            return;
         }
         this.waiting.visible = false;
         this.btnSkipVideo.removeEventListener(FocusEvent.FOCUS_OUT,this.onBtnFocusOutHandler);
         this.btnSkipVideo.visible = false;
         this._videoCompleted = true;
         if(param1)
         {
            onSkipButtonClickedS();
         }
         else
         {
            onVideoCompleteS();
         }
      }
      
      private function onSkipVideoButtonClickHandler(param1:ButtonEvent) : void
      {
         this.btnSkipVideo.removeEventListener(FocusEvent.FOCUS_OUT,this.onBtnFocusOutHandler);
         this.onSkip();
      }
      
      private function onVideoPlayerPlaybackStoppedHandler(param1:VideoPlayerEvent) : void
      {
         this.completeVideo();
      }
      
      private function onVideoPlayerStatusChangedHandler(param1:VideoPlayerStatusEvent) : void
      {
         if(this.videoPlayer.status == PlayerStatus.PLAYING)
         {
            this.videoPlayer.removeEventListener(VideoPlayerStatusEvent.STATUS_CHANGED,this.onVideoPlayerStatusChangedHandler);
            onVideoStartedS();
            this.videoPlayer.seek(0);
         }
      }
      
      private function onVideoPlayerErrorHandler(param1:VideoPlayerStatusEvent) : void
      {
         DebugUtils.LOG_ERROR(VIDEO_ERROR,param1.errorCode);
         this.completeVideo();
      }
      
      private function onBtnFocusOutHandler(param1:FocusEvent) : void
      {
         FocusManager.setFocus(this.btnSkipVideo);
      }
      
      public function as_setCurrentSubtitle(param1:String) : void
      {
         this._subtitleText = param1;
         invalidate(SUBTITLE_CHANGE);
      }
      
      private function onBreakPointChangedHandler(param1:StageSizeMangerEvent) : void
      {
         invalidate(BREAK_POINT);
      }
      
      public function as_handleKeydown() : void
      {
         if(!this.btnSkipVideo.visible && !this._videoCompleted)
         {
            App.utils.scheduler.scheduleOnNextFrame(this.showSkip);
         }
      }
   }
}
