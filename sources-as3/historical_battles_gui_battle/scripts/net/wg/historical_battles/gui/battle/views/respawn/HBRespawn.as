package net.wg.historical_battles.gui.battle.views.respawn
{
   import flash.text.TextField;
   import flash.text.TextFormat;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.events.UILoaderEvent;
   import net.wg.historical_battles.gui.battle.constants.HB_STAGE_SIZE;
   import net.wg.historical_battles.gui.battle.views.respawn.components.HBDivision;
   import net.wg.historical_battles.gui.battle.views.respawn.components.HBLine;
   import net.wg.historical_battles.gui.battle.views.respawn.components.HBTimerResp;
   import net.wg.historical_battles.gui.battle.views.respawn.components.card.HBVehicleContainer;
   import net.wg.historical_battles.gui.battle.views.respawn.constants.HB_RESPAWN_PROPS;
   import net.wg.historical_battles.gui.battle.views.respawn.data.HBRespawnVO;
   import net.wg.historical_battles.gui.battle.views.respawn.data.HBTimerRespVO;
   import net.wg.historical_battles.gui.battle.views.respawn.events.HBRespawnEvent;
   import net.wg.historical_battles.gui.battle.views.respawn.events.HBVehicleCardEvent;
   import net.wg.historical_battles.infrastructure.base.meta.IHBRespawnMeta;
   import net.wg.historical_battles.infrastructure.base.meta.impl.HBRespawnMeta;
   
   public class HBRespawn extends HBRespawnMeta implements IHBRespawnMeta
   {
      
      private static const BACKGROUND_WIDTH:uint = 1920;
      
      private static const BACKGROUND_HEIGHT:uint = 1080;
      
      private static const BACKGROUND_ASPECT_RATIO:Number = BACKGROUND_WIDTH / BACKGROUND_HEIGHT;
       
      
      public var timer:HBTimerResp = null;
      
      public var division:HBDivision = null;
      
      public var vehicleContainer:HBVehicleContainer = null;
      
      public var line:HBLine = null;
      
      public var bg:UILoaderAlt = null;
      
      public var goalTimeTF:TextField = null;
      
      private var _data:HBRespawnVO = null;
      
      private var _stageWidth:uint = 0;
      
      private var _stageHeight:uint = 0;
      
      private var _goalTime:String = "";
      
      public function HBRespawn()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.line.setMode(HBLine.MODE_FOOTER);
         this.bg.addEventListener(UILoaderEvent.COMPLETE,this.onBgCompleteHandler);
         addEventListener(HBVehicleCardEvent.VEHICLE_PICK,this.onVehiclePickHandler);
         addEventListener(HBVehicleCardEvent.VEHICLE_SELECT,this.onVehicleSelectHandler);
      }
      
      override protected function setData(param1:HBRespawnVO) : void
      {
         if(this._data != param1)
         {
            this._data = param1;
            this.division.update(this._data.divisionVO);
            this.vehicleContainer.update(this._data.vehicleCards);
            this.bg.source = RES_ICONS_HISTORICAL_BATTLES.getMapBg(this._data.mapName);
            invalidateSize();
         }
      }
      
      override protected function setTimerData(param1:HBTimerRespVO) : void
      {
         this.timer.update(param1);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._data)
         {
            if(isInvalid(InvalidationType.DATA))
            {
               this.goalTimeTF.text = this._goalTime;
               invalidateSize();
            }
            if(this._stageWidth > 0 && this._stageHeight > 0 && isInvalid(InvalidationType.SIZE))
            {
               this.validateLayout();
            }
         }
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(HBVehicleCardEvent.VEHICLE_PICK,this.onVehiclePickHandler);
         removeEventListener(HBVehicleCardEvent.VEHICLE_SELECT,this.onVehicleSelectHandler);
         this.bg.removeEventListener(UILoaderEvent.COMPLETE,this.onBgCompleteHandler);
         this.bg.dispose();
         this.bg = null;
         this.timer.dispose();
         this.timer = null;
         this.division.dispose();
         this.division = null;
         this.vehicleContainer.dispose();
         this.vehicleContainer = null;
         this.line.dispose();
         this.line = null;
         this.goalTimeTF = null;
         this._data = null;
         super.onDispose();
      }
      
      public function as_setVisibility(param1:Boolean, param2:Boolean) : void
      {
         this.timer.ownerVisibleChange(param1);
         setCompVisible(param1);
         dispatchEvent(new HBRespawnEvent(HBRespawnEvent.VISIBILITY_CHANGE,param1,param2));
      }
      
      public function as_updateGoalTime(param1:String) : void
      {
         if(this._goalTime != param1)
         {
            this._goalTime = param1;
            invalidateData();
         }
      }
      
      public function updateSize(param1:uint, param2:uint) : void
      {
         var _loc3_:int = 0;
         if(this._stageWidth != param1 || this._stageHeight != param2)
         {
            this._stageWidth = param1;
            this._stageHeight = param2;
            _loc3_ = HB_STAGE_SIZE.getStageSize(param1,param2);
            this.division.updateSize(_loc3_);
            this.timer.updateSize(_loc3_);
            this.vehicleContainer.updateSize(_loc3_);
            invalidateSize();
         }
      }
      
      private function validateLayout() : void
      {
         this.updateBg();
         var _loc1_:int = HB_STAGE_SIZE.getStageSize(this._stageWidth,this._stageHeight);
         this.timer.x = this._stageWidth - this.timer.width >> 1;
         this.timer.y = HB_RESPAWN_PROPS.getTimerY(_loc1_);
         this.division.x = this._stageWidth - this.division.width >> 1;
         this.division.y = HB_RESPAWN_PROPS.getDivisionY(_loc1_);
         this.vehicleContainer.x = this._stageWidth - this.vehicleContainer.width >> 1;
         this.vehicleContainer.y = HB_RESPAWN_PROPS.getVehiclesY(_loc1_);
         this.line.updateSize(_loc1_);
         this.line.x = this._stageWidth - this.line.width >> 1;
         this.line.y = HB_RESPAWN_PROPS.getLineY(_loc1_);
         var _loc2_:TextFormat = this.goalTimeTF.getTextFormat();
         _loc2_.size = HB_RESPAWN_PROPS.getGoalTimeFontSize(_loc1_);
         this.goalTimeTF.setTextFormat(_loc2_);
         this.goalTimeTF.x = this._stageWidth - this.goalTimeTF.width | 0;
         this.goalTimeTF.y = HB_RESPAWN_PROPS.getGoalTimeY(_loc1_);
      }
      
      private function updateBg() : void
      {
         this.bg.width = this._stageHeight * BACKGROUND_ASPECT_RATIO;
         this.bg.height = this._stageHeight;
         if(this.bg.width < this._stageWidth)
         {
            this.bg.width = this._stageWidth;
         }
         this.bg.x = this._stageWidth - this.bg.width >> 1;
      }
      
      private function onBgCompleteHandler(param1:UILoaderEvent) : void
      {
         this.updateBg();
      }
      
      private function onVehiclePickHandler(param1:HBVehicleCardEvent) : void
      {
         onPickVehicleS(param1.vehicleId);
      }
      
      private function onVehicleSelectHandler(param1:HBVehicleCardEvent) : void
      {
         onSelectVehicleS();
      }
   }
}
