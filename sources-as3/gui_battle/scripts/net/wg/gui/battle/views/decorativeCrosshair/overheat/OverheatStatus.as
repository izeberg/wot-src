package net.wg.gui.battle.views.decorativeCrosshair.overheat
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.views.decorativeCrosshair.OverheatDecorativeCrosshair;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class OverheatStatus extends MovieClip implements IDisposable
   {
      
      private static const STATUS_SPEED_LIMIT:String = "speedLimit";
      
      private static const STATUS_RELOADING:String = "reloading";
      
      private static const STATUS_WARNING:String = "warning";
       
      
      public var icon:OverheatSpeedLimitIcon = null;
      
      private var _isDisposed:Boolean = false;
      
      private var _speedLimit:int = -1;
      
      public function OverheatStatus()
      {
         super();
      }
      
      public function setState(param1:uint) : void
      {
         switch(param1)
         {
            case OverheatDecorativeCrosshair.STATE_DT_LOOSE:
            case OverheatDecorativeCrosshair.STATE_STACK_LOOSE:
            case OverheatDecorativeCrosshair.STATE_CHARGE_MIN:
               this.icon.visible = true;
               this.setStatusSpeedLimit();
               break;
            case OverheatDecorativeCrosshair.STATE_NO_SHELL_IN_CHAMBER:
               this.icon.visible = true;
               this.icon.gotoAndStop(STATUS_RELOADING);
               break;
            case OverheatDecorativeCrosshair.STATE_CHARGE_MAX:
            case OverheatDecorativeCrosshair.STATE_DT_GAIN:
            case OverheatDecorativeCrosshair.STATE_STACK_GAIN:
               this.icon.visible = false;
               break;
            default:
               this.icon.visible = true;
               this.icon.gotoAndStop(STATUS_WARNING);
         }
      }
      
      public function setSpeed(param1:int) : void
      {
         this._speedLimit = param1;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function dispose() : void
      {
         this._isDisposed = true;
         this.icon = null;
      }
      
      private function setStatusSpeedLimit() : void
      {
         this.icon.gotoAndStop(STATUS_SPEED_LIMIT);
         this.icon.setText(this._speedLimit.toString());
      }
   }
}
