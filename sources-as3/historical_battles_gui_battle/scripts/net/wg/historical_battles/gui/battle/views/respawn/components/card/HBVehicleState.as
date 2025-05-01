package net.wg.historical_battles.gui.battle.views.respawn.components.card
{
   import net.wg.historical_battles.gui.battle.constants.HB_STAGE_SIZE;
   import net.wg.historical_battles.gui.battle.views.respawn.components.HBTextBase;
   
   public class HBVehicleState extends HBTextBase
   {
      
      private static const FONT_SIZE:Object = {};
      
      {
         FONT_SIZE[HB_STAGE_SIZE.EXTRA_SMALL] = 10;
         FONT_SIZE[HB_STAGE_SIZE.SMALL] = 12;
         FONT_SIZE[HB_STAGE_SIZE.MEDIUM] = 14;
         FONT_SIZE[HB_STAGE_SIZE.LARGE] = 16;
         FONT_SIZE[HB_STAGE_SIZE.EXTRA_LARGE] = 20;
      }
      
      private var _size:uint = 0;
      
      public function HBVehicleState()
      {
         super();
      }
      
      public function updateSize(param1:uint) : void
      {
         if(this._size != param1)
         {
            this._size = param1;
            fontSize = FONT_SIZE[this._size];
         }
      }
   }
}
