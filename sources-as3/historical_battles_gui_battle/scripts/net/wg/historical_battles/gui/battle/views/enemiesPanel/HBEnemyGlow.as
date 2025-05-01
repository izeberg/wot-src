package net.wg.historical_battles.gui.battle.views.enemiesPanel
{
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class HBEnemyGlow extends SimpleDisposable
   {
      
      public static const RED:String = "red";
      
      public static const PURPLE:String = "purple";
       
      
      private var _isBlindEnabled:Boolean = false;
      
      public function HBEnemyGlow()
      {
         super();
      }
      
      public function set isBlindEnabled(param1:Boolean) : void
      {
         if(this._isBlindEnabled == param1)
         {
            return;
         }
         this._isBlindEnabled = param1;
         gotoAndStop(!!this._isBlindEnabled ? PURPLE : RED);
      }
   }
}
