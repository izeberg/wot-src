package net.wg.portal.gui.battle.views.enemiesPanel
{
   import fl.motion.easing.Cubic;
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Values;
   import net.wg.portal.infrastructure.base.meta.IPortalEnemiesPanelMeta;
   import net.wg.portal.infrastructure.base.meta.impl.PortalEnemiesPanelMeta;
   import scaleform.clik.motion.Tween;
   
   public class EnemiesPanel extends PortalEnemiesPanelMeta implements IPortalEnemiesPanelMeta
   {
      
      private static const SPACE:String = " ";
      
      private static const SEPARATOR:String = " / ";
      
      private static const BUFF_STATUS_TF_OFFSET_Y:int = 15;
      
      private static const BUFF_STATUS_BG_OFFSET_Y:int = 11;
      
      private static const NORTH_LANE_INDEX:int = 1;
      
      private static const MID_LANE_INDEX:int = 2;
      
      private static const SOUTH_LANE_INDEX:int = 3;
      
      private static const NORTH_LANE:uint = InvalidationType.SYSTEM_FLAGS_BORDER << NORTH_LANE_INDEX;
      
      private static const MID_LANE:uint = InvalidationType.SYSTEM_FLAGS_BORDER << MID_LANE_INDEX;
      
      private static const SOUTH_LANE:uint = InvalidationType.SYSTEM_FLAGS_BORDER << SOUTH_LANE_INDEX;
      
      private static const LANE_PHASE:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 4;
      
      private static const BUFF_STATUS:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 5;
      
      private static const APPEARANCE_TWEEN_DURATION:uint = 850;
       
      
      public var phaseInfoTf:TextField = null;
      
      public var northLane:LaneVehiclesRenderer = null;
      
      public var midLane:LaneVehiclesRenderer = null;
      
      public var southLane:LaneVehiclesRenderer = null;
      
      public var buffStatusTf:TextField = null;
      
      public var buffStatusBg:MovieClip = null;
      
      private var _currentPhase:int = 0;
      
      private var _phasesCount:int = 0;
      
      private var _midLaneOriginY:int = 0;
      
      private var _southLaneOriginY:int = 0;
      
      private var _buffStatusTfVisible:Boolean = false;
      
      private var _phaseInfoTfAppearanceTween:Tween = null;
      
      private var _buffStatusTfAppearanceTween:Tween = null;
      
      private var _buffStatusBgAppearanceTween:Tween = null;
      
      public function EnemiesPanel()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this._midLaneOriginY = this.midLane.y;
         this._southLaneOriginY = this.southLane.y;
      }
      
      override protected function draw() : void
      {
         if(isInvalid(LANE_PHASE))
         {
            if(this._phasesCount > 0)
            {
               this.phaseInfoTf.text = PORTAL_EVENT.BATTLE_PHASE_LABEL;
               this.phaseInfoTf.appendText(SPACE + this._currentPhase + SEPARATOR + this._phasesCount);
               if(this.phaseInfoTf.alpha == 0)
               {
                  this.clearPhaseInfoTfAppearanceTween();
                  this._phaseInfoTfAppearanceTween = new Tween(APPEARANCE_TWEEN_DURATION,this.phaseInfoTf,{"alpha":1},{"ease":Cubic.easeInOut});
               }
            }
            else
            {
               this.clearPhaseInfoTfAppearanceTween();
               this.phaseInfoTf.alpha = 0;
               this.phaseInfoTf.text = Values.EMPTY_STR;
            }
         }
         if(this.northLane.hasInfo && isInvalid(NORTH_LANE))
         {
            this.validateLaneRenderer(this.northLane);
         }
         if(this.midLane.hasInfo && isInvalid(MID_LANE))
         {
            this.validateLaneRenderer(this.midLane);
         }
         if(this.southLane.hasInfo && isInvalid(SOUTH_LANE))
         {
            this.validateLaneRenderer(this.southLane);
         }
         if(isInvalid(BUFF_STATUS))
         {
            this.buffStatusTf.visible = this._buffStatusTfVisible;
            this.buffStatusBg.visible = this._buffStatusTfVisible;
            if(this._buffStatusTfVisible)
            {
               this.clearBuffStatusAppearanceTween();
               if(this.buffStatusTf.alpha < 1)
               {
                  this._buffStatusTfAppearanceTween = new Tween(APPEARANCE_TWEEN_DURATION,this.buffStatusTf,{"alpha":1},{"ease":Cubic.easeInOut});
                  this._buffStatusBgAppearanceTween = new Tween(APPEARANCE_TWEEN_DURATION,this.buffStatusBg,{"alpha":1},{"ease":Cubic.easeInOut});
               }
            }
            else
            {
               this.buffStatusTf.alpha = 0;
               this.buffStatusBg.alpha = 0;
            }
            if(this._buffStatusTfVisible)
            {
               this.updatebuffStatusTfY();
            }
         }
         super.draw();
      }
      
      override protected function onDispose() : void
      {
         this.clearPhaseInfoTfAppearanceTween();
         this.clearBuffStatusAppearanceTween();
         this.phaseInfoTf = null;
         this.northLane.dispose();
         this.northLane = null;
         this.midLane.dispose();
         this.midLane = null;
         this.southLane.dispose();
         this.southLane = null;
         this.buffStatusTf = null;
         this.buffStatusBg = null;
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.buffStatusTf.text = PORTAL_EVENT.BATTLE_STATUS_BUFF;
         this.buffStatusTf.visible = false;
         this.northLane.setNameLabel(PORTAL_EVENT.BATTLE_LANE_LABEL_NORTH);
         this.northLane.visible = false;
         this.midLane.setNameLabel(PORTAL_EVENT.BATTLE_LANE_LABEL_MID);
         this.midLane.visible = false;
         this.southLane.setNameLabel(PORTAL_EVENT.BATTLE_LANE_LABEL_SOUTH);
         this.southLane.visible = false;
      }
      
      public function as_resetState() : void
      {
         this.northLane.visible = false;
         this.northLane.reset();
         this.midLane.y = this._midLaneOriginY;
         this.midLane.visible = false;
         this.midLane.reset();
         this.southLane.y = this._southLaneOriginY;
         this.southLane.visible = false;
         this.southLane.reset();
      }
      
      public function as_setBuffStatusVisible(param1:Boolean) : void
      {
         this._buffStatusTfVisible = param1;
         invalidate(BUFF_STATUS);
      }
      
      public function as_setCurrentPhase(param1:int) : void
      {
         this._currentPhase = param1;
         invalidate(LANE_PHASE);
      }
      
      public function as_setLaneVehicleInfo(param1:int, param2:int, param3:int, param4:int) : void
      {
         switch(param1)
         {
            case NORTH_LANE_INDEX:
               this.invalidateLaneRenderer(this.northLane,NORTH_LANE);
               this.updateLaneRenderer(this.northLane,param2,param3,param4);
               break;
            case MID_LANE_INDEX:
               this.invalidateLaneRenderer(this.midLane,MID_LANE);
               this.updateLaneRenderer(this.midLane,param2,param3,param4);
               break;
            case SOUTH_LANE_INDEX:
               this.invalidateLaneRenderer(this.southLane,SOUTH_LANE);
               this.updateLaneRenderer(this.southLane,param2,param3,param4);
               this.southLane.setVehicleInfo(param2,param3,param4);
         }
      }
      
      public function as_setPhasesCount(param1:int) : void
      {
         this._phasesCount = param1;
         invalidate(LANE_PHASE);
      }
      
      private function clearPhaseInfoTfAppearanceTween() : void
      {
         if(this._phaseInfoTfAppearanceTween)
         {
            this._phaseInfoTfAppearanceTween.dispose();
            this._phaseInfoTfAppearanceTween = null;
         }
      }
      
      private function clearBuffStatusAppearanceTween() : void
      {
         if(this._buffStatusTfAppearanceTween)
         {
            this._buffStatusTfAppearanceTween.dispose();
            this._buffStatusTfAppearanceTween = null;
         }
         if(this._buffStatusBgAppearanceTween)
         {
            this._buffStatusBgAppearanceTween.dispose();
            this._buffStatusBgAppearanceTween = null;
         }
      }
      
      private function invalidateLaneRenderer(param1:LaneVehiclesRenderer, param2:uint) : void
      {
         if(!param1.hasInfo)
         {
            invalidate(param2);
         }
      }
      
      private function updateLaneRenderer(param1:LaneVehiclesRenderer, param2:int, param3:int, param4:int) : void
      {
         param1.setVehicleInfo(param2,param3,param4);
      }
      
      private function validateLaneRenderer(param1:LaneVehiclesRenderer) : void
      {
         param1.visible = true;
         this.updateLanesY();
         this.updatebuffStatusTfY();
         param1.playAppearanceTween();
      }
      
      private function updateLanesY() : void
      {
         if(this.northLane.visible && this.midLane.visible && this.southLane.visible)
         {
            this.midLane.y = this._midLaneOriginY;
            this.southLane.y = this._southLaneOriginY;
         }
         else if(this.northLane.visible && this.midLane.visible)
         {
            this.midLane.y = this._midLaneOriginY;
         }
         else if(this.northLane.visible && this.southLane.visible)
         {
            this.southLane.y = this._midLaneOriginY;
         }
         else if(this.midLane.visible && this.southLane.visible)
         {
            this.midLane.y = this.northLane.y;
            this.southLane.y = this._midLaneOriginY;
         }
         else if(this.midLane.visible)
         {
            this.midLane.y = this.northLane.y;
         }
         else if(this.southLane.visible)
         {
            this.southLane.y = this.northLane.y;
         }
      }
      
      private function updatebuffStatusTfY() : void
      {
         var _loc1_:int = this.phaseInfoTf.y + this.phaseInfoTf.height;
         if(this.northLane.visible && this.midLane.visible && this.southLane.visible)
         {
            _loc1_ = this._southLaneOriginY + this.southLane.height;
         }
         else if(this.northLane.visible && this.midLane.visible || this.northLane.visible && this.southLane.visible || this.midLane.visible && this.southLane.visible)
         {
            _loc1_ = this._midLaneOriginY + this.midLane.height;
         }
         else if(this.northLane.visible || this.midLane.visible || this.southLane.visible)
         {
            _loc1_ = this.northLane.y + this.northLane.height;
         }
         this.buffStatusTf.y = _loc1_ + BUFF_STATUS_TF_OFFSET_Y;
         this.buffStatusBg.y = this.buffStatusTf.y - BUFF_STATUS_BG_OFFSET_Y;
      }
   }
}
