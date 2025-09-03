package net.wg.gui.battle.views.decorativeCrosshair.overheat
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.views.decorativeCrosshair.OverheatDecorativeCrosshair;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class OverheatDecoration extends MovieClip implements IDisposable
   {
      
      private static const ANIM_SHOW_OVERHEAT:String = "show";
      
      private static const ANIM_HIDE_OVERHEAT:String = "hide";
      
      private static const SNIPER_STATE:uint = 1;
      
      private static const ARCADE_STATE:uint = 2;
       
      
      public var asset:MovieClip = null;
      
      private var _isDisposed:Boolean = false;
      
      private var _isOverheatVisible:Boolean = false;
      
      public function OverheatDecoration()
      {
         super();
      }
      
      public function setState(param1:uint, param2:uint) : void
      {
         if(param2 == OverheatDecorativeCrosshair.STATE_CHARGE_MAX && !this._isOverheatVisible)
         {
            this._isOverheatVisible = true;
            gotoAndPlay(ANIM_SHOW_OVERHEAT);
         }
         else if(param2 == OverheatDecorativeCrosshair.STATE_STACK_LOOSE && param1 == OverheatDecorativeCrosshair.STATE_DT_LOOSE || param2 == OverheatDecorativeCrosshair.STATE_NO_SHELL_IN_CHAMBER)
         {
            if(this._isOverheatVisible)
            {
               this._isOverheatVisible = false;
               gotoAndPlay(ANIM_HIDE_OVERHEAT);
            }
         }
      }
      
      public function setMode(param1:Boolean) : void
      {
         this.asset.gotoAndStop(!!param1 ? SNIPER_STATE : ARCADE_STATE);
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function dispose() : void
      {
         this.asset = null;
         this._isDisposed = true;
      }
   }
}
