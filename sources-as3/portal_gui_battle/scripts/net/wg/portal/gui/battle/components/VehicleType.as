package net.wg.portal.gui.battle.components
{
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.infrastructure.interfaces.IImage;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class VehicleType extends BattleUIComponent
   {
      
      private static const PATH:String = "img://portal/gui/maps/icons/vehicleTypes/flat/";
      
      private static const SLASH:String = "/";
      
      private static const PNG:String = ".png";
      
      public static const ORANGE:String = "orange";
      
      public static const RED:String = "red";
      
      public static const GREY:String = "grey";
      
      public static const PURPLE:String = "purple";
      
      public static const WHITE:String = "white";
      
      public static const SIZE_16:String = "16x16";
      
      public static const SIZE_24:String = "24x24";
       
      
      public var icon:IImage = null;
      
      private var _vehicleType:String = "";
      
      private var _color:String = "red";
      
      private var _size:String = "16x16";
      
      public function VehicleType()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.icon.dispose();
         this.icon = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(StringUtils.isNotEmpty(this._vehicleType) && isInvalid(InvalidationType.DATA))
         {
            this.icon.source = PATH + this._color + SLASH + this._size + SLASH + this._vehicleType + PNG;
         }
      }
      
      public function get vehicleType() : String
      {
         return this._vehicleType;
      }
      
      public function set vehicleType(param1:String) : void
      {
         if(this._vehicleType == param1)
         {
            return;
         }
         this._vehicleType = param1;
         invalidateData();
      }
      
      public function get color() : String
      {
         return this._color;
      }
      
      public function set color(param1:String) : void
      {
         if(this._color == param1)
         {
            return;
         }
         this._color = param1;
         invalidateData();
      }
      
      public function get size() : String
      {
         return this._size;
      }
      
      public function set size(param1:String) : void
      {
         if(this._size == param1)
         {
            return;
         }
         this._size = param1;
         invalidateData();
      }
   }
}
