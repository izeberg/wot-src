package net.wg.gui.components.questProgress.components.metrics.rangeValues
{
   import flash.text.TextField;
   import net.wg.data.constants.generated.QUEST_PROGRESS_BASE;
   import net.wg.gui.components.questProgress.components.metrics.QPMetricsCmptBase;
   import net.wg.gui.components.questProgress.data.metrics.QPMetricsVehicleRangeVO;
   import net.wg.gui.components.questProgress.interfaces.data.IQPMetrics;
   import net.wg.utils.ICommons;
   import scaleform.gfx.TextFieldEx;
   
   public class VehiclesMetricsRangeValuesComponentBase extends QPMetricsCmptBase
   {
      
      protected static const VALUES_SEPARATOR:String = "/";
      
      protected static const GOAL_GAP:int = 0;
      
      protected static const VALUE_GAP:int = 0;
       
      
      public var valueTf:TextField = null;
      
      public var separatorTf:TextField = null;
      
      public var goalTf:TextField = null;
      
      protected var commons:ICommons;
      
      public function VehiclesMetricsRangeValuesComponentBase()
      {
         this.commons = App.utils.commons;
         super();
      }
      
      override protected function doPrepare() : void
      {
         TextFieldEx.setNoTranslate(this.valueTf,true);
         TextFieldEx.setNoTranslate(this.separatorTf,true);
         TextFieldEx.setNoTranslate(this.goalTf,true);
         this.separatorTf.text = VALUES_SEPARATOR;
         this.commons.updateTextFieldSize(this.separatorTf,true,false);
         super.doPrepare();
      }
      
      override protected final function onInit(param1:IQPMetrics) : void
      {
         this.doInit(QPMetricsVehicleRangeVO(param1));
         super.onInit(param1);
      }
      
      override protected final function onUpdate(param1:IQPMetrics) : void
      {
         this.doUpdate(QPMetricsVehicleRangeVO(param1));
         super.onUpdate(param1);
      }
      
      override protected function onDispose() : void
      {
         this.commons = null;
         this.valueTf = null;
         this.separatorTf = null;
         this.goalTf = null;
         super.onDispose();
      }
      
      protected function doInit(param1:QPMetricsVehicleRangeVO) : void
      {
         this.updateValueGoal(param1.value,param1.goal);
      }
      
      protected function doUpdate(param1:QPMetricsVehicleRangeVO) : void
      {
         this.updateValueGoal(param1.value,param1.goal);
      }
      
      protected function updateValueGoal(param1:String, param2:String) : void
      {
         this.valueTf.text = param1;
         this.goalTf.text = param2;
         this.commons.updateTextFieldSize(this.valueTf,true,false);
         this.commons.updateTextFieldSize(this.goalTf,true,false);
      }
      
      override protected function doUpdateState(param1:int) : void
      {
         super.doUpdateState(param1);
         var _loc2_:uint = !!isCompleted ? uint(QUEST_PROGRESS_BASE.QP_TEXT_COLOR_STATE_COMPLETED_VALUE) : uint(QUEST_PROGRESS_BASE.QP_TEXT_COLOR_STATE_IN_PROGRESS_VALUE);
         var _loc3_:uint = !!isCompleted ? uint(QUEST_PROGRESS_BASE.QP_TEXT_COLOR_STATE_COMPLETED) : uint(QUEST_PROGRESS_BASE.QP_TEXT_COLOR_STATE_IN_PROGRESS);
         this.valueTf.textColor = _loc2_;
         this.separatorTf.textColor = _loc3_;
         this.goalTf.textColor = _loc3_;
      }
   }
}
