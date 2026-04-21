package net.wg.gui.battle.views.widgetsPanel
{
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.generated.CROSSHAIR_VIEW_ID;
   import net.wg.data.constants.generated.LOW_CHARGE_SHOT_CONSTS;
   import net.wg.gui.battle.views.widgetsPanel.lowChargeShot.FirstStageTimeField;
   import net.wg.gui.battle.views.widgetsPanel.lowChargeShot.QuickReloadTimeField;
   import net.wg.gui.battle.views.widgetsPanel.lowChargeShot.SecondStageTimeField;
   import net.wg.gui.battle.views.widgetsPanel.lowChargeShot.TimeField;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot.ColorsProvider;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot.LowChargeShotReloadController;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot.LowChargeShotReloadEvent;
   import net.wg.infrastructure.base.meta.ILowChargeShotWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.LowChargeShotWidgetMeta;
   
   public class LowChargeShotWidget extends LowChargeShotWidgetMeta implements ILowChargeShotWidgetMeta
   {
      
      private static const MECHANICS_SNIPER_RIGHT_X:int = -240;
      
      private static const MECHANICS_ARCADE_RIGHT_X:int = -160;
       
      
      public var firstStageTimerTF:FirstStageTimeField = null;
      
      public var secondStageTimerTF:SecondStageTimeField = null;
      
      public var quickReloadingTimerTF:QuickReloadTimeField = null;
      
      private var _currentStageTimerTF:TimeField = null;
      
      private var _reloadController:LowChargeShotReloadController;
      
      private var _colors:ColorsProvider;
      
      private var _reloadingState:Number = -1;
      
      public function LowChargeShotWidget()
      {
         this._reloadController = new LowChargeShotReloadController();
         this._colors = new ColorsProvider();
         super();
         this.firstStageTimerTF.colorsProvider = this._colors;
         this.secondStageTimerTF.colorsProvider = this._colors;
         this.quickReloadingTimerTF.colorsProvider = this._colors;
         this.firstStageTimerTF.setReloadingState(LOW_CHARGE_SHOT_CONSTS.STATE_NONE);
         this.secondStageTimerTF.setReloadingState(LOW_CHARGE_SHOT_CONSTS.STATE_NONE);
         this.quickReloadingTimerTF.setReloadingState(LOW_CHARGE_SHOT_CONSTS.STATE_NONE);
      }
      
      override protected function onDispose() : void
      {
         this.firstStageTimerTF.dispose();
         this.firstStageTimerTF = null;
         this.secondStageTimerTF.dispose();
         this.secondStageTimerTF = null;
         this.quickReloadingTimerTF.dispose();
         this.quickReloadingTimerTF = null;
         this._currentStageTimerTF = null;
         this._colors.dispose();
         this._colors = null;
         this._reloadController.removeEventListener(LowChargeShotReloadEvent.TICK,this.onReloadControllerChangedHandler);
         this._reloadController.removeEventListener(LowChargeShotReloadEvent.QUICK_RELOAD_CHANGED,this.onReloadControllerChangedHandler);
         this._reloadController.dispose();
         this._reloadController = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         if(isInvalid(InvalidationType.SIZE))
         {
            if(crosshairType == CROSSHAIR_VIEW_ID.ARCADE)
            {
               x = MECHANICS_ARCADE_RIGHT_X;
            }
            else if(crosshairType == CROSSHAIR_VIEW_ID.SNIPER)
            {
               x = MECHANICS_SNIPER_RIGHT_X;
            }
         }
         super.draw();
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         this._reloadController.addEventListener(LowChargeShotReloadEvent.TICK,this.onReloadControllerChangedHandler);
         this._reloadController.addEventListener(LowChargeShotReloadEvent.QUICK_RELOAD_CHANGED,this.onReloadControllerChangedHandler);
      }
      
      public function as_setInitialTime(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number) : void
      {
         if(this._reloadController.trySetInitialTime(param1,param2,param3,param4,param5))
         {
            this.setReloadingState(this._reloadingState,true);
         }
      }
      
      public function as_setTimeLeft(param1:Number, param2:Number, param3:Boolean) : void
      {
         this._reloadController.setTimeLeft(param1,param2,param3);
      }
      
      private function setReloadingState(param1:Number, param2:Boolean = false) : void
      {
         if(this._reloadingState != param1 || param2)
         {
            this._currentStageTimerTF = this.secondStageTimerTF;
            switch(param1)
            {
               case LOW_CHARGE_SHOT_CONSTS.LOW_CHARGE:
                  this.firstStageTimerTF.setValue(this._reloadController.lowChargeTime);
                  this.secondStageTimerTF.setValue(this._reloadController.currentTimeLeft);
                  break;
               case LOW_CHARGE_SHOT_CONSTS.ALMOST_FINISHED:
                  this.firstStageTimerTF.setValue(this._reloadController.lowChargeTime);
                  this.secondStageTimerTF.setValue(this._reloadController.currentTimeLeft);
                  break;
               case LOW_CHARGE_SHOT_CONSTS.FULL_CHARGE:
                  this.firstStageTimerTF.setValue(this._reloadController.baseTime,false);
                  this.quickReloadingTimerTF.setValue(this._reloadController.quickReloadingTime,false);
                  break;
               case LOW_CHARGE_SHOT_CONSTS.QUICK_RELOAD:
                  this._currentStageTimerTF = this.firstStageTimerTF;
                  break;
               default:
                  this.firstStageTimerTF.setValue(this._reloadController.lowChargeTime);
                  this.secondStageTimerTF.setValue(this._reloadController.restChargeTime);
                  this._currentStageTimerTF = this.firstStageTimerTF;
            }
            this._reloadingState = param1;
            this.firstStageTimerTF.setReloadingState(this._reloadingState);
            this.secondStageTimerTF.setReloadingState(this._reloadingState);
            this.quickReloadingTimerTF.setReloadingState(this._reloadingState);
         }
      }
      
      private function onReloadControllerChangedHandler(param1:LowChargeShotReloadEvent) : void
      {
         var _loc2_:Boolean = false;
         this.setReloadingState(param1.state);
         if(this._currentStageTimerTF && param1.time >= 0)
         {
            _loc2_ = this._reloadingState != LOW_CHARGE_SHOT_CONSTS.QUICK_RELOAD;
            this._currentStageTimerTF.setValue(param1.time,_loc2_);
         }
      }
   }
}
