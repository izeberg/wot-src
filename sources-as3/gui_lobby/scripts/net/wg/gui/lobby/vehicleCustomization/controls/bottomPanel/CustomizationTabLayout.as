package net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel
{
   import flash.display.BitmapData;
   import flash.geom.Point;
   import net.wg.data.constants.Linkages;
   import net.wg.gui.components.containers.GroupLayout;
   
   public class CustomizationTabLayout extends GroupLayout
   {
       
      
      private var _delimiterBitmapData:BitmapData = null;
      
      public function CustomizationTabLayout(param1:int = 0)
      {
         super();
         this.gap = param1;
         var _loc2_:Class = App.utils.classFactory.getClass(Linkages.CUSTOMIZATION_TAB_GROUP_DELIMITER);
         this._delimiterBitmapData = new _loc2_();
      }
      
      override public function invokeLayout() : Object
      {
         var _loc1_:CustomizationBottomPanelTabButton = null;
         var _loc5_:Number = NaN;
         var _loc8_:int = 0;
         _target.graphics.clear();
         var _loc2_:int = _target.numChildren;
         var _loc3_:int = 0;
         var _loc4_:uint = 0;
         var _loc6_:int = this.gap;
         var _loc7_:int = 0;
         while(_loc7_ < _loc2_)
         {
            _loc1_ = _target.getChildAt(_loc7_) as CustomizationBottomPanelTabButton;
            _loc1_.x = _loc4_ + _loc1_.marginLeft | 0;
            _loc4_ = _loc1_.x + _loc1_.width + _loc6_;
            _loc5_ = _loc1_.height;
            if(_loc1_.marginLeft)
            {
               _loc8_ = _loc1_.marginLeft + _loc6_;
               _target.graphics.beginBitmapFill(this._delimiterBitmapData);
               _target.graphics.drawRect(_loc1_.x - _loc8_,0,_loc8_,_loc5_);
               _target.graphics.endFill();
            }
            if(_loc3_ < _loc5_)
            {
               _loc3_ = _loc5_;
            }
            _loc7_++;
         }
         if(_loc4_ > 0)
         {
            _loc4_ -= _loc6_;
         }
         return new Point(_loc4_,_loc3_);
      }
      
      override public function dispose() : void
      {
         super.dispose();
         this._delimiterBitmapData.dispose();
         this._delimiterBitmapData = null;
      }
   }
}
