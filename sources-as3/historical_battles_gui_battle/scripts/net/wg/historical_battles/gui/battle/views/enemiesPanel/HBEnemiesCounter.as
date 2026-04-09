package net.wg.historical_battles.gui.battle.views.enemiesPanel
{
   import flash.text.TextField;
   
   public class HBEnemiesCounter extends HBEnemyGlow
   {
       
      
      public var counterTF:TextField = null;
      
      private var _count:int = 0;
      
      public function HBEnemiesCounter()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.counterTF = null;
         super.onDispose();
      }
      
      public function set count(param1:int) : void
      {
         if(this._count == param1)
         {
            return;
         }
         this._count = param1;
         this.counterTF.text = "+" + this._count;
      }
   }
}
