package net.wg.gui.battle.views.widgetsPanel.stanceDance
{
   import flash.display.FrameLabel;
   import flash.utils.Dictionary;
   import net.wg.gui.battle.views.widgetsPanel.BaseVehicleMechanicsWidget;
   import net.wg.gui.battle.views.widgetsPanel.StanceDanceButtonsContainer;
   
   public class StanceDanceWidget extends BaseVehicleMechanicsWidget
   {
       
      
      public var hotKeysContainer:StanceDanceButtonsContainer = null;
      
      private var _targetState:String = "";
      
      private var _labelMaps:Dictionary;
      
      public function StanceDanceWidget()
      {
         this._labelMaps = new Dictionary();
         super();
      }
      
      private function hasLabel(param1:String) : Boolean
      {
         var _loc2_:Object = this._labelMaps[crosshairType];
         if(!_loc2_)
         {
            _loc2_ = this.collectLabels();
            this._labelMaps[crosshairType] = _loc2_;
         }
         return Boolean(_loc2_[param1]);
      }
      
      private function collectLabels() : Object
      {
         var _loc2_:FrameLabel = null;
         var _loc1_:Object = {};
         if(this.hotKeysContainer && this.hotKeysContainer.currentLabels)
         {
            for each(_loc2_ in this.hotKeysContainer.currentLabels)
            {
               _loc1_[_loc2_.name] = true;
            }
         }
         return _loc1_;
      }
      
      override public function as_setState(param1:String, param2:Boolean) : void
      {
         this._targetState = param1;
         super.as_setState(param1,param2);
      }
      
      protected function updateButtonsState(param1:Boolean) : void
      {
         var _loc2_:String = !!param1 ? this._targetState + INSTANTLY_POSTFIX : this._targetState;
         var _loc3_:String = crosshairType + "_" + _loc2_;
         var _loc4_:Boolean = this.hasLabel(_loc3_);
         var _loc5_:String = !!_loc4_ ? _loc3_ : _loc2_;
         if(param1)
         {
            this.hotKeysContainer.gotoAndStop(_loc5_);
         }
         else
         {
            this.hotKeysContainer.gotoAndPlay(_loc5_);
         }
      }
      
      override protected function onDispose() : void
      {
         this.hotKeysContainer.dispose();
         this.hotKeysContainer = null;
         App.utils.data.cleanupDynamicObject(this._labelMaps);
         this._labelMaps = null;
         super.onDispose();
      }
   }
}
