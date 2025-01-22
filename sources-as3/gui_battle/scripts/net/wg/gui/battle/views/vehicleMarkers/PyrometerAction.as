package net.wg.gui.battle.views.vehicleMarkers
{
   import flash.display.MovieClip;
   import flash.utils.clearTimeout;
   import flash.utils.setTimeout;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class PyrometerAction extends ActionAnim implements IDisposable
   {
      
      private static const FRAME_RED:String = "red";
      
      private static const FRAME_GREEN:String = "green";
      
      private static const FRAME_PURPLE:String = "purple";
      
      private static const ALLY_FRAME:String = "ally";
      
      private static const ENEMY_FRAME:String = "enemy";
      
      private static const ENEMY_BLIND_FRAME:String = "enemyBlind";
       
      
      public var circle:MovieClip = null;
      
      public var icon:MovieClip = null;
      
      private var _timeout:int = 0;
      
      public function PyrometerAction()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.cancelTimeout();
         this.circle = null;
         this.icon = null;
         super.onDispose();
      }
      
      override protected function animComplete() : void
      {
         this.cancelTimeout();
         super.animComplete();
      }
      
      public function showByDuration(param1:int) : void
      {
         this.cancelTimeout();
         this._timeout = setTimeout(this.hideByTimeout,param1);
         show();
      }
      
      private function hideByTimeout() : void
      {
         hideAnim();
      }
      
      private function cancelTimeout() : void
      {
         if(visible && this._timeout > 0)
         {
            clearTimeout(this._timeout);
         }
         this._timeout = 0;
      }
      
      public function set isAlly(param1:Boolean) : void
      {
         var _loc4_:Boolean = false;
         var _loc2_:String = ALLY_FRAME;
         var _loc3_:String = FRAME_GREEN;
         if(!param1)
         {
            _loc4_ = VehicleMarkersManager.getInstance().isColorBlind;
            _loc2_ = !!_loc4_ ? ENEMY_BLIND_FRAME : ENEMY_FRAME;
            _loc3_ = !!_loc4_ ? FRAME_PURPLE : FRAME_RED;
         }
         this.icon.gotoAndStop(_loc2_);
         this.circle.gotoAndStop(_loc3_);
      }
   }
}
