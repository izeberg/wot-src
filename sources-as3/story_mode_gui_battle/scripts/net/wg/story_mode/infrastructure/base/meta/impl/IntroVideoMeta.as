package net.wg.story_mode.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.infrastructure.base.AbstractView;
   import net.wg.infrastructure.exceptions.AbstractException;
   import net.wg.story_mode.battle.views.intro.data.IntroVideoVO;
   
   public class IntroVideoMeta extends AbstractView
   {
       
      
      public var onVideoStarted:Function;
      
      public var onVideoComplete:Function;
      
      public var onSkipButtonVisible:Function;
      
      public var onSkipButtonClicked:Function;
      
      private var _introVideoVO:IntroVideoVO;
      
      public function IntroVideoMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._introVideoVO)
         {
            this._introVideoVO.dispose();
            this._introVideoVO = null;
         }
         super.onDispose();
      }
      
      public function onVideoStartedS() : void
      {
         App.utils.asserter.assertNotNull(this.onVideoStarted,"onVideoStarted" + Errors.CANT_NULL);
         this.onVideoStarted();
      }
      
      public function onVideoCompleteS() : void
      {
         App.utils.asserter.assertNotNull(this.onVideoComplete,"onVideoComplete" + Errors.CANT_NULL);
         this.onVideoComplete();
      }
      
      public function onSkipButtonVisibleS() : void
      {
         App.utils.asserter.assertNotNull(this.onSkipButtonVisible,"onSkipButtonVisible" + Errors.CANT_NULL);
         this.onSkipButtonVisible();
      }
      
      public function onSkipButtonClickedS() : void
      {
         App.utils.asserter.assertNotNull(this.onSkipButtonClicked,"onSkipButtonClicked" + Errors.CANT_NULL);
         this.onSkipButtonClicked();
      }
      
      public final function as_setData(param1:Object) : void
      {
         var _loc2_:IntroVideoVO = this._introVideoVO;
         this._introVideoVO = new IntroVideoVO(param1);
         this.setData(this._introVideoVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setData(param1:IntroVideoVO) : void
      {
         var _loc2_:String = "as_setData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
