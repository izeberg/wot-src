package net.wg.gui.notification.custom.pm3
{
   import flash.display.Sprite;
   import flash.text.TextField;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.notification.custom.vo.PM3QuestVehicleVO;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class PM3VehicleInfo extends Sprite implements IDisposable
   {
      
      private static const ELITE_POSTFIX:String = "_elite";
      
      private static const VEHICLE_TYPE_LEFT_MARGIN:int = 0;
      
      private static const VEHICLE_TYPE_ELITE_LEFT_MARGIN:int = 5;
      
      private static const NAME_LEFT_MARGIN:int = -7;
      
      private static const NAME_ELITE_LEFT_MARGIN:int = -2;
      
      private static const LINE_LEFT_SHIFT:int = 0;
      
      private static const LINE_RIGHT_SHIFT:int = 5;
       
      
      public var levelTF:TextField = null;
      
      public var nameTF:TextField = null;
      
      public var vehType:UILoaderAlt = null;
      
      public var crossLine:Sprite = null;
      
      private var _isDisposed:Boolean = false;
      
      public function PM3VehicleInfo()
      {
         super();
      }
      
      public final function dispose() : void
      {
         this.vehType.dispose();
         this.vehType = null;
         this.levelTF = null;
         this.nameTF = null;
         this.crossLine = null;
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function setData(param1:PM3QuestVehicleVO) : void
      {
         this.levelTF.text = param1.levelRoman;
         this.nameTF.text = param1.userName;
         var _loc2_:String = RES_ICONS.getVehicleTypes24x24(param1.type,!!param1.isPrem ? ELITE_POSTFIX : "");
         this.vehType.source = _loc2_;
         this.vehType.x = this.levelTF.textWidth + (!!param1.isPrem ? VEHICLE_TYPE_ELITE_LEFT_MARGIN : VEHICLE_TYPE_LEFT_MARGIN) >> 0;
         this.nameTF.x = this.vehType.width + this.vehType.x + (!!param1.isPrem ? NAME_ELITE_LEFT_MARGIN : NAME_LEFT_MARGIN);
         this.crossLine.x = this.levelTF.x - LINE_LEFT_SHIFT;
         this.crossLine.width = this.width - this.levelTF.x + LINE_RIGHT_SHIFT + LINE_LEFT_SHIFT >> 0;
      }
      
      override public function get width() : Number
      {
         return this.nameTF.x + this.nameTF.textWidth >> 0;
      }
   }
}
