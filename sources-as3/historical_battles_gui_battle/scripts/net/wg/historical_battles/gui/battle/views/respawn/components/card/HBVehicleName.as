package net.wg.historical_battles.gui.battle.views.respawn.components.card
{
   import net.wg.historical_battles.gui.battle.constants.HB_STAGE_SIZE;
   import net.wg.historical_battles.gui.battle.views.respawn.components.HBTextBase;
   import net.wg.infrastructure.interfaces.IImage;
   
   public class HBVehicleName extends HBTextBase
   {
      
      private static const FONT_SIZE:Object = {};
      
      private static const ICON_SCALE:Object = {};
      
      private static const ICON_Y:Object = {};
      
      private static const ICON_ORIGINAL_SIZE:uint = 36;
      
      {
         FONT_SIZE[HB_STAGE_SIZE.EXTRA_SMALL] = 14;
         FONT_SIZE[HB_STAGE_SIZE.SMALL] = 14;
         FONT_SIZE[HB_STAGE_SIZE.MEDIUM] = 16;
         FONT_SIZE[HB_STAGE_SIZE.LARGE] = 16;
         FONT_SIZE[HB_STAGE_SIZE.EXTRA_LARGE] = 20;
         ICON_SCALE[HB_STAGE_SIZE.EXTRA_SMALL] = 0.43;
         ICON_SCALE[HB_STAGE_SIZE.SMALL] = 0.46;
         ICON_SCALE[HB_STAGE_SIZE.MEDIUM] = 0.53;
         ICON_SCALE[HB_STAGE_SIZE.LARGE] = 0.66;
         ICON_SCALE[HB_STAGE_SIZE.EXTRA_LARGE] = 0.86;
         ICON_Y[HB_STAGE_SIZE.EXTRA_SMALL] = 3;
         ICON_Y[HB_STAGE_SIZE.SMALL] = 3;
         ICON_Y[HB_STAGE_SIZE.MEDIUM] = 3;
         ICON_Y[HB_STAGE_SIZE.LARGE] = 0;
         ICON_Y[HB_STAGE_SIZE.EXTRA_LARGE] = -1;
      }
      
      public var typeIcon:IImage = null;
      
      private var _size:uint = 0;
      
      public function HBVehicleName()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.typeIcon.dispose();
         this.typeIcon = null;
         super.onDispose();
      }
      
      public function updateSize(param1:uint) : void
      {
         if(this._size != param1)
         {
            this._size = param1;
            fontSize = FONT_SIZE[this._size];
            this.typeIcon.scaleX = this.typeIcon.scaleY = ICON_SCALE[this._size];
            textField.x = ICON_ORIGINAL_SIZE * ICON_SCALE[this._size] | 0;
            this.typeIcon.y = ICON_Y[this._size];
         }
      }
      
      override public function get width() : Number
      {
         return textField.x + textField.width | 0;
      }
      
      public function set typeSrc(param1:String) : void
      {
         this.typeIcon.source = param1;
      }
   }
}
