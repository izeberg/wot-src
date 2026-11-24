package net.wg.gui.battle.views.minimap.components.entries.vehicle
{
   import flash.geom.Point;
   import flash.text.TextField;
   import net.wg.gui.battle.views.minimap.MinimapEntryController;
   import net.wg.gui.battle.views.minimap.components.entries.interfaces.IVehicleMinimapEntry;
   import net.wg.gui.battle.views.minimap.constants.MinimapSizeConst;
   
   public class MinimapEntryLabelHelper
   {
      
      private static const HP_OFFSET_X:int = 8;
      
      private static const HP_OFFSET_Y:int = -2;
      
      private static const OFFSET_Y_BETWEEN_TEXT_AND_BORDER:int = 3;
       
      
      private var _bounds:Point;
      
      private var _entryRef:IVehicleMinimapEntry;
      
      private var _initialOffsetX:int;
      
      private var _initialOffsetY:int;
      
      private var _hpOffsetX:int;
      
      private var _hpOffsetY:int;
      
      private var _isSuspended:Boolean = true;
      
      private var _isRegistered:Boolean = false;
      
      private var _sizeIndex:int;
      
      private var _currentTF:TextField;
      
      private var __prevEntityX:Number = 0;
      
      private var __prevEntityY:Number = 0;
      
      private var _tfWidthOnScreen:Number = 0;
      
      private var _tfHeightOnScreen:Number = 0;
      
      public function MinimapEntryLabelHelper(param1:IVehicleMinimapEntry, param2:TextField)
      {
         this._bounds = new Point(MinimapSizeConst.MAP_SIZE[0].width / 2,MinimapSizeConst.MAP_SIZE[0].height / 2);
         super();
         this._entryRef = param1;
         this._initialOffsetX = param2.x;
         this._initialOffsetY = param2.y;
         this._hpOffsetX = this._initialOffsetX + HP_OFFSET_X;
         this._hpOffsetY = this._initialOffsetY + HP_OFFSET_Y;
         this.setCurrentTF(param2);
      }
      
      public final function dispose() : void
      {
         if(this._isRegistered)
         {
            MinimapEntryController.instance.unregisterActiveLabelHelper(this);
            this._isRegistered = false;
         }
         this._currentTF = null;
         this._entryRef = null;
         this._bounds = null;
      }
      
      public function forceUpdate() : void
      {
         this.update(true);
      }
      
      public function setCurrentTF(param1:TextField) : void
      {
         this._currentTF = param1;
         this.recalcTFScreenParameters();
         this.forceUpdate();
      }
      
      public function suspend(param1:Boolean) : void
      {
         this._isSuspended = param1;
         this.validateState();
      }
      
      public function timerUpdate() : void
      {
         this.update();
      }
      
      public function updateSizeIndex(param1:int) : void
      {
         this._sizeIndex = param1;
         this.recalcTFScreenParameters();
         this.forceUpdate();
      }
      
      public function validateLabel() : void
      {
         this.recalcTFScreenParameters();
         this.validateState();
      }
      
      private function validateState() : void
      {
         if(!this._isSuspended && this._entryRef.isVehicleLabelVisible)
         {
            if(!this._isRegistered)
            {
               MinimapEntryController.instance.registerActiveLabelHelper(this);
               this._isRegistered = true;
            }
         }
         else
         {
            if(this._isRegistered)
            {
               MinimapEntryController.instance.unregisterActiveLabelHelper(this);
               this._isRegistered = false;
            }
            this.__prevEntityX = 0;
            this.__prevEntityY = 0;
         }
         this.forceUpdate();
      }
      
      private function update(param1:Boolean = false) : void
      {
         var _loc2_:int = 0;
         var _loc3_:int = 0;
         if(!this._entryRef.isVehicleLabelVisible)
         {
            return;
         }
         if(param1 || this.__prevEntityX != this._entryRef.x || this.__prevEntityY != this._entryRef.y)
         {
            this.__prevEntityX = this._entryRef.x;
            this.__prevEntityY = this._entryRef.y;
            if(this._entryRef.isHpCircleVisible)
            {
               _loc2_ = this._hpOffsetX;
               _loc3_ = this._hpOffsetY;
            }
            else
            {
               _loc2_ = this._initialOffsetX;
               _loc3_ = this._initialOffsetY;
            }
            if(!this._isSuspended && this._entryRef.x + this._tfWidthOnScreen + _loc2_ > this._bounds.x)
            {
               this._currentTF.x = -(this._currentTF.width + _loc2_);
            }
            else
            {
               this._currentTF.x = _loc2_;
            }
            if(!this._isSuspended && this._entryRef.y + this._tfHeightOnScreen + _loc3_ > this._bounds.y)
            {
               this._currentTF.y = -this._currentTF.height + OFFSET_Y_BETWEEN_TEXT_AND_BORDER;
            }
            else if(!this._isSuspended && this._entryRef.y < -this._bounds.y - HP_OFFSET_Y)
            {
               this._currentTF.y = this._initialOffsetY;
            }
            else
            {
               this._currentTF.y = _loc3_;
            }
         }
      }
      
      private function recalcTFScreenParameters() : void
      {
         var _loc1_:Number = MinimapSizeConst.ENTRY_SCALES[this._sizeIndex];
         var _loc2_:Number = MinimapSizeConst.ENTRY_CONTR_SCALES[this._sizeIndex];
         this._tfWidthOnScreen = this._currentTF.width;
         this._tfWidthOnScreen *= _loc2_;
         this._tfWidthOnScreen /= _loc1_;
         this._tfHeightOnScreen = this._currentTF.height;
         this._tfHeightOnScreen *= _loc2_;
         this._tfHeightOnScreen /= _loc1_;
      }
   }
}
