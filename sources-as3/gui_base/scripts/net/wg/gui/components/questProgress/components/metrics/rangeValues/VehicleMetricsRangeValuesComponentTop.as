package net.wg.gui.components.questProgress.components.metrics.rangeValues
{
   import net.wg.data.constants.Linkages;
   import net.wg.gui.components.questProgress.QuestProgressAtlasSprite;
   import net.wg.gui.components.questProgress.data.metrics.QPMetricsVehicleRangeVO;
   
   public class VehicleMetricsRangeValuesComponentTop extends VehiclesMetricsRangeValuesComponentBase
   {
      
      protected static const ICONS_WIDTH:int = 15;
       
      
      protected var vehicles:Vector.<QuestProgressAtlasSprite> = null;
      
      private var _pool:Vector.<QuestProgressAtlasSprite> = null;
      
      private var _imageYPosLine:int = 40;
      
      public function VehicleMetricsRangeValuesComponentTop()
      {
         super();
      }
      
      override protected function doLayout() : void
      {
         if(!isCompleted)
         {
            separatorTf.x = -(separatorTf.width >> 1);
            valueTf.x = separatorTf.x - valueTf.width - VALUE_GAP;
            goalTf.x = separatorTf.x + separatorTf.width + GOAL_GAP;
         }
         componentWidth = valueTf.x + valueTf.width + separatorTf.width + goalTf.width + VALUE_GAP + GOAL_GAP;
         var _loc1_:int = this.vehicles.length;
         var _loc2_:Number = -(_loc1_ * ICONS_WIDTH - ICONS_WIDTH) / 2;
         var _loc3_:int = 0;
         while(_loc3_ < _loc1_)
         {
            this.vehicles[_loc3_].x = _loc2_ ^ 0;
            _loc2_ += ICONS_WIDTH;
            _loc3_++;
         }
         super.doLayout();
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:QuestProgressAtlasSprite = null;
         if(this.vehicles)
         {
            for each(_loc1_ in this.vehicles)
            {
               this.removeChild(_loc1_);
            }
            this.vehicles.splice(0,this.vehicles.length);
            this.vehicles = null;
         }
         if(this._pool)
         {
            this._pool.splice(0,this._pool.length);
            this._pool = null;
         }
         valueTf = null;
         super.onDispose();
      }
      
      override protected function doInit(param1:QPMetricsVehicleRangeVO) : void
      {
         this.vehicles = new Vector.<QuestProgressAtlasSprite>();
         this._pool = new Vector.<QuestProgressAtlasSprite>();
         this.updateValue(param1.value);
         super.doInit(param1);
      }
      
      override protected function doUpdate(param1:QPMetricsVehicleRangeVO) : void
      {
         this.updateValue(param1.value);
         this.updateVehicles(param1.vehicleTypes);
         super.doUpdate(param1);
      }
      
      override protected function doUpdateState(param1:int) : void
      {
         var _loc2_:QuestProgressAtlasSprite = null;
         for each(_loc2_ in this.vehicles)
         {
            _loc2_.visible = !isCompleted;
         }
         super.doUpdateState(param1);
      }
      
      protected function updateValue(param1:String) : void
      {
         valueTf.text = param1;
      }
      
      private function updateVehicles(param1:Vector.<String>) : void
      {
         var _loc2_:int = 0;
         var _loc3_:int = param1.length;
         var _loc4_:int = _loc3_ - this.vehicles.length;
         if(_loc4_ > 0)
         {
            _loc2_ = 0;
            while(_loc2_ < _loc4_)
            {
               this.vehicles.push(this.getCmpnt());
               _loc2_++;
            }
         }
         else if(_loc4_ < 0)
         {
            _loc4_ *= -1;
            _loc2_ = 0;
            while(_loc2_ < _loc4_)
            {
               this.removeCmpnt(this.vehicles.pop());
               _loc2_++;
            }
         }
         _loc4_ = this.vehicles.length;
         _loc2_ = 0;
         while(_loc2_ < _loc4_)
         {
            this.vehicles[_loc2_].imageName = param1[_loc2_];
            _loc2_++;
         }
      }
      
      private function getCmpnt() : QuestProgressAtlasSprite
      {
         var _loc1_:QuestProgressAtlasSprite = null;
         if(this._pool.length)
         {
            _loc1_ = this._pool.pop();
         }
         else
         {
            _loc1_ = App.utils.classFactory.getComponent(Linkages.QP_ATLAS_SPRITE,QuestProgressAtlasSprite);
            _loc1_.isCentralize = true;
            _loc1_.y = this._imageYPosLine;
         }
         this.addChild(_loc1_);
         return _loc1_;
      }
      
      private function removeCmpnt(param1:QuestProgressAtlasSprite) : void
      {
         this.removeChild(param1);
         this._pool.push(param1);
      }
   }
}
