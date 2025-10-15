package net.wg.gui.battle.views.vehicleMarkers
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.text.TextField;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class StatTrackMarker extends SimpleDisposable
   {
      
      public static const ON_HIDDEN:String = "onHidden";
       
      
      public var fadeIn:MovieClip = null;
      
      public var fadeOut:MovieClip = null;
      
      public var idle:MovieClip = null;
      
      private var _textFields:Vector.<TextField> = null;
      
      public function StatTrackMarker()
      {
         super();
         this.hide(true);
         this.fadeIn.visible = this.fadeOut.visible = this.idle.visible = false;
         this.fadeIn.addFrameScript(this.fadeIn.totalFrames - 1,this.onFadeInAnimationComplete);
         this.fadeOut.addFrameScript(this.fadeOut.totalFrames - 1,this.onFadeOutAnimationComplete);
         this._textFields = new <TextField>[this.fadeIn.stat.valueTF,this.fadeOut.stat.valueTF,this.idle.stat.valueTF];
      }
      
      override protected function onDispose() : void
      {
         this.hide(true);
         this.fadeIn.addFrameScript(this.fadeIn.totalFrames - 1,null);
         this.fadeIn = null;
         this.fadeOut.addFrameScript(this.fadeOut.totalFrames - 1,null);
         this.fadeOut = null;
         this.idle = null;
         this._textFields.splice(0,this._textFields.length);
         this._textFields = null;
         super.onDispose();
      }
      
      private function onFadeInAnimationComplete() : void
      {
         this.show(true);
      }
      
      private function onFadeOutAnimationComplete() : void
      {
         this.hide(true);
      }
      
      public function show(param1:Boolean = false) : void
      {
         this.fadeIn.visible = this.fadeOut.visible = false;
         if(param1)
         {
            this.idle.visible = true;
            this.idle.gotoAndPlay(1);
         }
         else
         {
            this.fadeIn.visible = true;
            this.fadeIn.gotoAndPlay(1);
         }
      }
      
      public function hide(param1:Boolean = false) : void
      {
         this.idle.stop();
         this.fadeIn.visible = this.fadeOut.visible = this.idle.visible = false;
         if(param1)
         {
            dispatchEvent(new Event(ON_HIDDEN));
         }
         else
         {
            this.fadeOut.visible = true;
            this.fadeOut.gotoAndPlay(1);
         }
      }
      
      public function updateStats(param1:String, param2:String) : void
      {
         var _loc3_:TextField = null;
         for each(_loc3_ in this._textFields)
         {
            _loc3_.text = param2;
         }
      }
      
      public function isAnimationPlaying() : Boolean
      {
         return this.fadeIn.visible || this.fadeOut.visible || this.idle.visible;
      }
   }
}
