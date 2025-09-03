package net.wg.gui.notification.custom.pm3
{
   import flash.display.Sprite;
   import flash.text.TextField;
   import net.wg.data.constants.Linkages;
   import net.wg.infrastructure.interfaces.IDisposableSprite;
   import net.wg.utils.IClassFactory;
   
   public class PM3DescriptionUncompleted extends Sprite implements IDisposableSprite
   {
      
      private static const ICON_STEP:int = 43;
      
      private static const INFO_STEP:int = 30;
      
      private static const X_CENTER:int = 288 >> 1;
      
      private static const FROM_Y:int = 83;
      
      private static const TEXT_BOTTOM_MARGIN:int = 0;
      
      private static const TEXT_ADDITIONAL_HEIGHT:int = 4;
      
      private static const ICON_TOP_MARGIN:int = -11;
       
      
      public var statusTF:TextField = null;
      
      private var _isDisposed:Boolean = false;
      
      private var _vehicleIcons:Array = null;
      
      private var _vehicleInfos:Array = null;
      
      private var _classFactory:IClassFactory = null;
      
      public function PM3DescriptionUncompleted()
      {
         super();
         this._classFactory = App.utils.classFactory;
      }
      
      public final function dispose() : void
      {
         var _loc1_:PM3VehicleIcon = null;
         var _loc2_:PM3VehicleInfo = null;
         if(this._vehicleIcons != null)
         {
            for each(_loc1_ in this._vehicleIcons)
            {
               _loc1_.dispose();
               this.removeChild(_loc1_);
            }
            this._vehicleIcons.length = 0;
            this._vehicleIcons = null;
         }
         if(this._vehicleInfos != null)
         {
            for each(_loc2_ in this._vehicleInfos)
            {
               _loc2_.dispose();
               this.removeChild(_loc2_);
            }
            this._vehicleInfos.length = 0;
            this._vehicleInfos = null;
         }
         this._classFactory = null;
         this.statusTF = null;
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function setData(param1:String, param2:Array, param3:int) : void
      {
         var _loc4_:PM3VehicleIcon = null;
         var _loc10_:Boolean = false;
         this.statusTF.htmlText = param1;
         this.statusTF.height = this.statusTF.textHeight + TEXT_ADDITIONAL_HEIGHT + TEXT_BOTTOM_MARGIN >> 0;
         _loc4_ = null;
         var _loc5_:PM3VehicleInfo = null;
         var _loc6_:int = X_CENTER - (ICON_STEP * (param3 - 1) >> 1);
         var _loc7_:int = this.statusTF.y + this.statusTF.height + ICON_TOP_MARGIN - TEXT_ADDITIONAL_HEIGHT;
         var _loc8_:int = FROM_Y;
         var _loc9_:int = param2.length;
         _loc10_ = false;
         this._vehicleIcons = [];
         this._vehicleInfos = [];
         var _loc11_:int = 0;
         while(_loc11_ < param3)
         {
            _loc10_ = _loc11_ < _loc9_;
            _loc4_ = this._classFactory.getComponent(Linkages.PM3_SYS_MES_DESCR_COMPLETED_VEH_UI,PM3VehicleIcon);
            _loc4_.x = _loc6_;
            _loc4_.y = _loc7_;
            _loc4_.isComplete = _loc10_;
            this.addChild(_loc4_);
            this._vehicleIcons.push(_loc4_);
            _loc6_ += ICON_STEP;
            if(_loc10_)
            {
               _loc5_ = this._classFactory.getComponent(Linkages.PM3_SYS_MES_DESCR_INFO_VEH_UI,PM3VehicleInfo);
               _loc5_.setData(param2[_loc11_]);
               _loc5_.x = X_CENTER - (_loc5_.width >> 1);
               _loc5_.y = _loc8_;
               this.addChild(_loc5_);
               this._vehicleInfos.push(_loc5_);
               _loc8_ += INFO_STEP;
            }
            _loc11_++;
         }
      }
   }
}
