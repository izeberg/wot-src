package net.wg.gui.components.questProgress.components.metrics.rangeValues
{
   import net.wg.data.constants.Linkages;
   import net.wg.gui.components.questProgress.QuestProgressAtlasSprite;
   import net.wg.gui.components.questProgress.data.metrics.QPMetricsVehicleRangeVO;
   
   public class VehiclesMetricsRangeValuesComponentTab extends VehiclesMetricsRangeValuesComponentBase
   {
      
      private static const IMAGE_Y_POSITION:int = 2;
      
      private static const VALUE_GAP:int = 10;
      
      private static const IMAGE_X_GAP:int = -8;
      
      private static const SEPARATOR_GAP:int = 0;
       
      
      private var _vehType:QuestProgressAtlasSprite = null;
      
      public function VehiclesMetricsRangeValuesComponentTab()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._vehType)
         {
            removeChild(this._vehType);
            this._vehType = null;
         }
         commons = null;
         super.onDispose();
      }
      
      override protected function doInit(param1:QPMetricsVehicleRangeVO) : void
      {
         super.doInit(param1);
         updateValueGoal(param1.currentValue,param1.currentGoal);
         this._vehType = App.utils.classFactory.getComponent(Linkages.QP_ATLAS_SPRITE,QuestProgressAtlasSprite);
         this._vehType.y = IMAGE_Y_POSITION;
         this._vehType.imageName = param1.vehType;
         addChild(this._vehType);
      }
      
      override protected function doUpdate(param1:QPMetricsVehicleRangeVO) : void
      {
         updateValueGoal(param1.currentValue,param1.currentGoal);
      }
      
      override protected function doLayout() : void
      {
         var _loc1_:int = Boolean(this._vehType) ? int(this._vehType.x + this._vehType.width + IMAGE_X_GAP) : int(0);
         valueTf.x = _loc1_ + VALUE_GAP;
         separatorTf.x = valueTf.x + valueTf.width + SEPARATOR_GAP;
         goalTf.x = separatorTf.x + separatorTf.width + GOAL_GAP;
         componentWidth = goalTf.x + goalTf.width;
         super.doLayout();
      }
   }
}
