package net.wg.gui.components.crosshairPanel.components.gunMarker.auxiliaryRocketLauncher
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import net.wg.infrastructure.base.SimpleContainer;
   
   public class AuxiliaryRocketLauncherGunMarkerTagClip extends SimpleContainer
   {
      
      private static const TAG_FRAME_PREFIX:String = "x";
      
      private static const ANIMATION_SHOW:String = "show";
      
      private static const ANIMATION_HIDE:String = "hide";
      
      private static const INSTANT_POSTFIX:String = "_instant";
       
      
      public var circle:MovieClip = null;
      
      private var _currentState:String = "hide";
      
      public function AuxiliaryRocketLauncherGunMarkerTagClip()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.circle = null;
         removeEventListener(Event.ENTER_FRAME,this.onAfterZoomFrameInit);
         super.onDispose();
      }
      
      public function setVisible(param1:Boolean) : void
      {
         this.setState(!!param1 ? ANIMATION_SHOW : ANIMATION_HIDE);
      }
      
      public function setZoomFactor(param1:Number) : void
      {
         gotoAndStop(TAG_FRAME_PREFIX + param1);
         this.setState(this._currentState,true);
         removeEventListener(Event.ENTER_FRAME,this.onAfterZoomFrameInit);
         addEventListener(Event.ENTER_FRAME,this.onAfterZoomFrameInit);
      }
      
      private function setState(param1:String, param2:Boolean = false) : void
      {
         if(param2)
         {
            this.circle.gotoAndStop(param1 + INSTANT_POSTFIX);
         }
         else
         {
            this.circle.gotoAndPlay(param1);
         }
         this._currentState = param1;
      }
      
      private function onAfterZoomFrameInit(param1:Event) : void
      {
         removeEventListener(Event.ENTER_FRAME,this.onAfterZoomFrameInit);
         this.setState(this._currentState,true);
      }
   }
}
