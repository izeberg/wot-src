package net.wg.portal.gui.battle.views.enemiesPanel
{
   import flash.display.BlendMode;
   import flash.text.TextField;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.portal.gui.battle.components.VehicleType;
   
   public class VehicleTypesAmount extends BattleDisplayable
   {
      
      private static const OUT_OF_VEHICLES_ALPHA:Number = 0.5;
      
      private static const HAS_VEHICLES_ALPHA:Number = 1;
       
      
      public var countTf:TextField = null;
      
      public var vehTypeRed:VehicleType = null;
      
      public var vehTypeGrey:VehicleType = null;
      
      private var _count:int = -1;
      
      public function VehicleTypesAmount()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.countTf = null;
         this.vehTypeRed.dispose();
         this.vehTypeRed = null;
         this.vehTypeGrey.dispose();
         this.vehTypeGrey = null;
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.vehTypeRed.color = VehicleType.RED;
         this.vehTypeRed.size = VehicleType.SIZE_24;
         this.vehTypeRed.blendMode = BlendMode.SCREEN;
         this.vehTypeGrey.color = VehicleType.GREY;
         this.vehTypeGrey.size = VehicleType.SIZE_24;
         this.vehTypeGrey.visible = false;
         this.vehTypeGrey.blendMode = BlendMode.SCREEN;
      }
      
      public function set vehicleType(param1:String) : void
      {
         this.vehTypeRed.vehicleType = param1;
         this.vehTypeGrey.vehicleType = param1;
      }
      
      public function get count() : int
      {
         return this._count;
      }
      
      public function set count(param1:int) : void
      {
         this.countTf.text = param1.toString();
         if(param1 == 0)
         {
            alpha = OUT_OF_VEHICLES_ALPHA;
            this.vehTypeGrey.visible = true;
            this.vehTypeRed.visible = false;
         }
         else
         {
            alpha = HAS_VEHICLES_ALPHA;
            this.vehTypeGrey.visible = false;
            this.vehTypeRed.visible = true;
         }
         this._count = param1;
      }
   }
}
