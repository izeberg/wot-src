package net.wg.historical_battles.gui.battle.components
{
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class HBVehicleType extends BattleAtlasSprite implements IDisposable
   {
      
      private static const PREFIX:String = "hb_";
      
      private static const DELIMITER:String = "_";
      
      public static const GREEN:String = "green";
      
      public static const ORANGE:String = "orange";
      
      public static const RED:String = "red";
      
      public static const PURPLE:String = "purple";
      
      public static const SIZE_16:String = "16x16";
      
      public static const SIZE_24:String = "24x24";
       
      
      private var _vehicleType:String = "";
      
      private var _color:String = "green";
      
      public function HBVehicleType()
      {
         super();
      }
      
      public function dispose() : void
      {
         App.utils.scheduler.cancelTask(this.draw);
      }
      
      public function isDisposed() : Boolean
      {
         return false;
      }
      
      protected function draw() : void
      {
         if(StringUtils.isNotEmpty(this._vehicleType))
         {
            imageName = PREFIX + this._color + DELIMITER + this._vehicleType;
         }
         App.utils.scheduler.cancelTask(this.draw);
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
         App.utils.scheduler.scheduleOnNextFrame(this.draw);
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
         App.utils.scheduler.scheduleOnNextFrame(this.draw);
      }
   }
}
