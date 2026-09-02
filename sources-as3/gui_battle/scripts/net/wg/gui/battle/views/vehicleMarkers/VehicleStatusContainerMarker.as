package net.wg.gui.battle.views.vehicleMarkers
{
   import fl.motion.easing.Linear;
   import flash.display.DisplayObject;
   import flash.events.Event;
   import flash.utils.Dictionary;
   import flash.utils.getDefinitionByName;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.BATTLE_MARKER_STATES;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.battle.views.vehicleMarkers.events.StatusAnimationEvent;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.FLSupplyObjectSelfRepairMarker;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleAnimatedStatusBaseMarker;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleBerserkerMarker;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleEngineerEffectMarker;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleFLBasicMarker;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleInspireMarker;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleInspireTargetMarker;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleSpecialAbilityMarker;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleStatusIconMarker;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleStatusMarker;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleStunMarker;
   import scaleform.clik.motion.Tween;
   
   public class VehicleStatusContainerMarker extends BattleUIComponent
   {
      
      private static const BASE_HEIGHT:int = 55;
      
      private static const MARKER_DEFAULT_X_POS:int = Values.ZERO;
      
      private static const MARKER_HORIZONTAL_OFFSET:int = 14;
      
      private static const MARKER_TWEEN_DURATION:int = 200;
      
      private static const FIELD_NAME_TO_SORT:String = "key";
       
      
      public var stealthMarker:VehicleFLBasicMarker = null;
      
      public var flRegenerationKitMarker:VehicleFLBasicMarker = null;
      
      public var baseEngineerMarker:VehicleEngineerEffectMarker = null;
      
      public var supplySelfRepairMarker:FLSupplyObjectSelfRepairMarker = null;
      
      public var inspireMarker:VehicleInspireMarker = null;
      
      public var inspireTargetMarker:VehicleInspireTargetMarker = null;
      
      public var healMarker:VehicleInspireMarker = null;
      
      public var stunMarker:VehicleStunMarker = null;
      
      public var berserkerMarker:VehicleBerserkerMarker = null;
      
      public var recoveryMarker:VehicleInspireTargetMarker = null;
      
      public var fireCircleMarker:VehicleAnimatedStatusBaseMarker = null;
      
      public var thunderStrikeMarker:VehicleAnimatedStatusBaseMarker = null;
      
      public var adaptationHealthRestoreMarker:VehicleStatusIconMarker = null;
      
      public var shotPassionMarker:VehicleStatusIconMarker = null;
      
      public var statusMarker:VehicleStatusMarker = null;
      
      private var _markerTweens:Vector.<Tween> = null;
      
      private var _statusEffectMarkers:Dictionary = null;
      
      private var _activeEffectID:int = -1;
      
      private var _oneShotStatusID:int = -1;
      
      private var _oneShotStatusPriority:int = -1;
      
      private var _separateMarkers:Dictionary = null;
      
      private var _currentSecondTxt:String = "";
      
      private var _currentColorName:String = "";
      
      private var _currentColorValue:uint = 0;
      
      public function VehicleStatusContainerMarker()
      {
         super();
         this._markerTweens = new Vector.<Tween>();
         this._statusEffectMarkers = new Dictionary();
         this.setupMarker(BATTLE_MARKER_STATES.STUN_STATE,this.stunMarker);
         this.setupMarker(BATTLE_MARKER_STATES.DEBUFF_STATE,this.stunMarker);
         this.setupMarker(BATTLE_MARKER_STATES.INSPIRING_STATE,this.inspireMarker);
         this.setupMarker(BATTLE_MARKER_STATES.INSPIRED_STATE,this.inspireTargetMarker);
         this.setupMarker(BATTLE_MARKER_STATES.ENGINEER_STATE,this.baseEngineerMarker);
         this.setupMarker(BATTLE_MARKER_STATES.HEALING_STATE,this.healMarker);
         this.setupMarker(BATTLE_MARKER_STATES.BERSERKER_STATE,this.berserkerMarker);
         this.setupMarker(BATTLE_MARKER_STATES.REPAIRING_STATE,this.recoveryMarker);
         this.setupMarker(BATTLE_MARKER_STATES.STEALTH_STATE,this.stealthMarker);
         this.setupMarker(BATTLE_MARKER_STATES.FL_REGENERATION_KIT_STATE,this.flRegenerationKitMarker);
         this.setupMarker(BATTLE_MARKER_STATES.FIRE_CIRCLE_STATE,this.fireCircleMarker);
         this.setupMarker(BATTLE_MARKER_STATES.THUNDER_STRIKE_STATE,this.thunderStrikeMarker);
         this.setupMarker(BATTLE_MARKER_STATES.SHOT_PASSION_STATE,this.shotPassionMarker);
         this.setupMarker(BATTLE_MARKER_STATES.ADAPTATION_HEALTH_RESTORE_STATE,this.adaptationHealthRestoreMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_RISKY_ATTACK_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_RISKY_ATTACK_HEAL_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_SNIPER_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_ALLY_SUPPORT_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_AOE_HEAL_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_HUNTER_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_CONCENTRATION_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_JUGGERNAUT_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_BERSERK_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_FAST_RECHARGE_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_SURE_SHOT_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_AOE_INSPIRE_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_ARTYLLERY_SUPPORT_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_MARCH_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_AGGRESSIVE_DETECTION_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.COMP7_POINT_RECON_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.CONFIRMED_STATE,this.statusMarker);
         this.setupMarker(BATTLE_MARKER_STATES.EPIC_SUPPLY_REPAIR_SELF_STATE,this.supplySelfRepairMarker);
         this._separateMarkers = new Dictionary();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.stunMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.baseEngineerMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.supplySelfRepairMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.inspireMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.inspireTargetMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.healMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.berserkerMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.recoveryMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.stealthMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.flRegenerationKitMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.fireCircleMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.thunderStrikeMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.shotPassionMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.adaptationHealthRestoreMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.statusMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.stunMarker.setupFrameEvents();
         this.baseEngineerMarker.setupFrameEvents();
         this.supplySelfRepairMarker.setupFrameEvents();
         this.inspireMarker.setupFrameEvents();
         this.inspireTargetMarker.setupFrameEvents();
         this.healMarker.setupFrameEvents();
         this.berserkerMarker.setupFrameEvents();
         this.recoveryMarker.setupFrameEvents();
         this.stealthMarker.setupFrameEvents();
         this.flRegenerationKitMarker.setupFrameEvents();
         this.fireCircleMarker.setupFrameEvents();
         this.thunderStrikeMarker.setupFrameEvents();
         this.shotPassionMarker.setupFrameEvents();
         this.adaptationHealthRestoreMarker.setupFrameEvents();
         this.statusMarker.setupFrameEvents();
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:* = undefined;
         var _loc2_:VehicleSpecialAbilityMarker = null;
         this.stunMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.baseEngineerMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.supplySelfRepairMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.inspireMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.inspireTargetMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.healMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.berserkerMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.recoveryMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.stealthMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.flRegenerationKitMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.fireCircleMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.thunderStrikeMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.shotPassionMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.adaptationHealthRestoreMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.statusMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.clearTweens();
         this._markerTweens = null;
         this.baseEngineerMarker.dispose();
         this.baseEngineerMarker = null;
         this.supplySelfRepairMarker.dispose();
         this.supplySelfRepairMarker = null;
         this.inspireMarker.dispose();
         this.inspireMarker = null;
         this.stunMarker.dispose();
         this.stunMarker = null;
         this.inspireTargetMarker.dispose();
         this.inspireTargetMarker = null;
         this.healMarker.dispose();
         this.healMarker = null;
         this.berserkerMarker.dispose();
         this.berserkerMarker = null;
         this.recoveryMarker.dispose();
         this.recoveryMarker = null;
         this.stealthMarker.dispose();
         this.stealthMarker = null;
         this.flRegenerationKitMarker.dispose();
         this.flRegenerationKitMarker = null;
         this.fireCircleMarker.dispose();
         this.fireCircleMarker = null;
         this.thunderStrikeMarker.dispose();
         this.thunderStrikeMarker = null;
         this.shotPassionMarker.dispose();
         this.shotPassionMarker = null;
         this.adaptationHealthRestoreMarker.dispose();
         this.adaptationHealthRestoreMarker = null;
         this.statusMarker.dispose();
         this.statusMarker = null;
         for(_loc1_ in this._statusEffectMarkers)
         {
            delete this._statusEffectMarkers[_loc1_];
         }
         this._statusEffectMarkers = null;
         for(_loc1_ in this._separateMarkers)
         {
            _loc2_ = this.getSeparateMarker(_loc1_);
            _loc2_.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onAbilityAnimationEventHiddenHandler);
            _loc2_.dispose();
            delete this._separateMarkers[_loc1_];
         }
         this._separateMarkers = null;
         super.onDispose();
      }
      
      public function hideMarker(param1:int, param2:int, param3:Boolean, param4:Boolean) : void
      {
         var _loc5_:VehicleAnimatedStatusBaseMarker = null;
         var _loc6_:VehicleAnimatedStatusBaseMarker = null;
         var _loc7_:VehicleStatusMarker = null;
         var _loc8_:VehicleAnimatedStatusBaseMarker = null;
         this._activeEffectID = param2;
         if(param1 > Values.DEFAULT_INT)
         {
            _loc5_ = this.getMarker(param1);
            if(_loc5_)
            {
               _loc5_.hideEffectTimer(param3);
            }
         }
         if(param2 > Values.DEFAULT_INT)
         {
            _loc6_ = this.getMarker(param2);
            if(_loc6_)
            {
               if(_loc6_.isAtlasSrcMode())
               {
                  _loc6_.setStatusID(param2);
                  _loc6_.updateAssets();
                  _loc7_ = _loc6_ as VehicleStatusMarker;
                  if(_loc7_)
                  {
                     _loc7_.switchTimerVisible(param4);
                  }
               }
               _loc6_.setVisibility(true);
               this.clearTweens();
            }
         }
         else
         {
            for each(_loc8_ in this._statusEffectMarkers)
            {
               if(this.getMarker(param1) != _loc8_)
               {
                  _loc8_.setVisibility(false);
               }
            }
         }
      }
      
      public function hideSeparateMarker(param1:int, param2:Boolean) : void
      {
         var _loc3_:VehicleSpecialAbilityMarker = this.getSeparateMarker(param1);
         if(_loc3_)
         {
            _loc3_.hideEffectTimer(param2);
         }
      }
      
      public function updateEffectTimer(param1:int, param2:Number, param3:Boolean = false) : void
      {
         var _loc4_:VehicleAnimatedStatusBaseMarker = this.getMarker(param1);
         if(_loc4_)
         {
            _loc4_.updateEffectTimer(param2,this._activeEffectID == param1,param3);
         }
         var _loc5_:VehicleSpecialAbilityMarker = this.getSeparateMarker(param1);
         if(_loc5_)
         {
            _loc5_.updateEffectTimer(param2,true,param3);
         }
      }
      
      public function isVisible() : Boolean
      {
         var _loc2_:* = undefined;
         var _loc1_:Boolean = false;
         var _loc3_:int = 0;
         var _loc4_:* = this._separateMarkers;
         for(_loc2_ in _loc4_)
         {
            _loc1_ = true;
         }
         return (this._activeEffectID == Values.DEFAULT_INT ? Boolean(false) : Boolean(this.getMarker(this._activeEffectID).isVisible())) || _loc1_;
      }
      
      public function setEffectColor(param1:String, param2:uint) : void
      {
         var _loc3_:* = undefined;
         this._currentColorName = param1;
         this._currentColorValue = param2;
         this.stunMarker.setEffectColor(param1,param2);
         this.baseEngineerMarker.setEffectColor(param1,param2);
         this.inspireMarker.setEffectColor(param1,param2);
         this.inspireTargetMarker.setEffectColor(param1,param2);
         this.healMarker.setEffectColor(param1,param2);
         this.berserkerMarker.setEffectColor(param1,param2);
         this.recoveryMarker.setEffectColor(param1,param2);
         this.stealthMarker.setEffectColor(param1,param2);
         this.flRegenerationKitMarker.setEffectColor(param1,param2);
         this.fireCircleMarker.setEffectColor(param1,param2);
         this.thunderStrikeMarker.setEffectColor(param1,param2);
         this.shotPassionMarker.setEffectColor(param1,param2);
         this.adaptationHealthRestoreMarker.setEffectColor(param1,param2);
         this.statusMarker.setEffectColor(param1,param2);
         for(_loc3_ in this._separateMarkers)
         {
            this.getSeparateMarker(_loc3_).setEffectColor(param1,param2);
         }
      }
      
      public function setSecondString(param1:String) : void
      {
         var _loc2_:* = undefined;
         this._currentSecondTxt = param1;
         this.stunMarker.setSecondString(param1);
         this.inspireMarker.setSecondString(param1);
         this.healMarker.setSecondString(param1);
         this.statusMarker.setSecondString(param1);
         for(_loc2_ in this._separateMarkers)
         {
            this.getSeparateMarker(_loc2_).setSecondString(param1);
         }
      }
      
      public function showMarker(param1:int, param2:int, param3:Boolean, param4:Number, param5:int, param6:int, param7:Boolean = true, param8:Boolean = true) : void
      {
         var _loc11_:VehicleAnimatedStatusBaseMarker = null;
         var _loc12_:VehicleAnimatedStatusBaseMarker = null;
         if(param2 > param6)
         {
            return;
         }
         var _loc9_:VehicleAnimatedStatusBaseMarker = this.getMarker(param1);
         var _loc10_:Boolean = false;
         if(this._activeEffectID != Values.DEFAULT_INT && this._activeEffectID != param1)
         {
            _loc11_ = this.getMarker(this._activeEffectID);
            if(_loc11_ != _loc9_)
            {
               _loc11_.setVisibility(false);
            }
            if(param1 != param5)
            {
               if(this._oneShotStatusID != Values.DEFAULT_INT && param2 < this._oneShotStatusPriority)
               {
                  _loc12_ = this.getMarker(this._oneShotStatusID);
                  if(_loc12_)
                  {
                     _loc12_.resetMarkerStates();
                  }
               }
               if(_loc9_)
               {
                  this._oneShotStatusID = param1;
                  this._oneShotStatusPriority = param2;
                  _loc10_ = true;
               }
            }
         }
         if(_loc9_)
         {
            if(_loc9_.isAtlasSrcMode())
            {
               _loc9_.setStatusID(param1);
               _loc9_.updateAssets();
            }
            _loc9_.showEffectTimer(param4,param3,_loc10_,param7,param8);
         }
         this._activeEffectID = param5;
         this.updateMarkersPositions(_loc9_);
      }
      
      public function showSeparateMarker(param1:int, param2:Boolean, param3:Number, param4:Boolean = true, param5:Boolean = true) : void
      {
         var _loc6_:VehicleSpecialAbilityMarker = this.getSeparateMarker(param1);
         if(_loc6_)
         {
            this.disposeSeparateMarker(param1);
         }
         var _loc7_:Class = getDefinitionByName(Linkages.VEHICLE_SPECIAL_ABILITY_MARKER_UI) as Class;
         _loc6_ = new _loc7_();
         if(_loc6_)
         {
            this.setupSeparateMarker(param1,_loc6_);
            _loc6_.setEffectColor(this._currentColorName,this._currentColorValue);
            _loc6_.setSecondString(this._currentSecondTxt);
            _loc6_.updateAssets();
            _loc6_.showEffectTimer(param3,param2,false,param4,param5);
            _loc6_.setupFrameEvents();
            _loc6_.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onAbilityAnimationEventHiddenHandler);
            addChild(_loc6_);
            this.updateMarkersPositions(_loc6_);
         }
      }
      
      protected function updateMarkersPositions(param1:DisplayObject = null) : void
      {
         var _loc2_:* = undefined;
         var _loc5_:VehicleAnimatedStatusBaseMarker = null;
         var _loc8_:int = 0;
         this.clearTweens();
         var _loc3_:Array = [];
         var _loc4_:VehicleAnimatedStatusBaseMarker = null;
         for(_loc2_ in this._separateMarkers)
         {
            _loc4_ = this.getSeparateMarker(_loc2_);
            _loc4_[FIELD_NAME_TO_SORT] = _loc2_;
            _loc3_.push(_loc4_);
         }
         _loc3_.sortOn(FIELD_NAME_TO_SORT,Array.NUMERIC | Array.DESCENDING);
         _loc5_ = this.getMarker(this._activeEffectID);
         if(_loc5_)
         {
            _loc3_.push(_loc5_);
         }
         var _loc6_:int = 0;
         var _loc7_:int = _loc3_.length;
         while(_loc6_ < _loc7_)
         {
            _loc4_ = _loc3_[_loc6_];
            _loc8_ = MARKER_HORIZONTAL_OFFSET * 2 * _loc6_ + MARKER_HORIZONTAL_OFFSET - MARKER_HORIZONTAL_OFFSET * _loc7_;
            if(param1 == _loc4_)
            {
               _loc4_.x = _loc8_;
            }
            else
            {
               this._markerTweens.push(new Tween(MARKER_TWEEN_DURATION,_loc4_,{"x":_loc8_},{"ease":Linear.easeOut}));
            }
            _loc6_++;
         }
      }
      
      protected function setupMarker(param1:int, param2:VehicleAnimatedStatusBaseMarker) : void
      {
         this._statusEffectMarkers[param1] = param2;
         param2.setStatusID(param1);
      }
      
      protected function getMarker(param1:int) : VehicleAnimatedStatusBaseMarker
      {
         return this._statusEffectMarkers[param1];
      }
      
      private function setupSeparateMarker(param1:int, param2:VehicleSpecialAbilityMarker) : void
      {
         this._separateMarkers[param1] = param2;
         param2.setStatusID(param1);
      }
      
      private function getSeparateMarker(param1:int) : VehicleSpecialAbilityMarker
      {
         return this._separateMarkers[param1];
      }
      
      override public function get height() : Number
      {
         return BASE_HEIGHT;
      }
      
      private function onStatusAnimationEventHiddenHandler(param1:StatusAnimationEvent) : void
      {
         var _loc2_:VehicleAnimatedStatusBaseMarker = null;
         if(param1.isOneShotAnimation)
         {
            this._oneShotStatusID = Values.DEFAULT_INT;
            this._oneShotStatusPriority = Values.DEFAULT_INT;
         }
         if(this._activeEffectID > Values.DEFAULT_INT)
         {
            _loc2_ = this.getMarker(this._activeEffectID);
            if(_loc2_)
            {
               _loc2_.setVisibility(true);
            }
         }
         else
         {
            DisplayObject(param1.currentTarget).x = MARKER_DEFAULT_X_POS;
         }
         this.updateMarkersPositions();
         dispatchEvent(new Event(Event.COMPLETE));
      }
      
      private function onAbilityAnimationEventHiddenHandler(param1:StatusAnimationEvent) : void
      {
         this.disposeSeparateMarker(param1.statusID);
      }
      
      private function disposeSeparateMarker(param1:int) : void
      {
         var _loc2_:VehicleSpecialAbilityMarker = this.getSeparateMarker(param1);
         if(_loc2_)
         {
            _loc2_.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onAbilityAnimationEventHiddenHandler);
            removeChild(_loc2_);
            _loc2_.dispose();
            delete this._separateMarkers[param1];
         }
         this.updateMarkersPositions();
         dispatchEvent(new Event(Event.COMPLETE));
      }
      
      private function clearTweens() : void
      {
         var _loc1_:int = 0;
         var _loc2_:int = 0;
         if(this._markerTweens)
         {
            _loc1_ = 0;
            _loc2_ = this._markerTweens.length;
            while(_loc1_ < _loc2_)
            {
               this._markerTweens[_loc1_].dispose();
               _loc1_++;
            }
            this._markerTweens.splice(0,_loc2_);
         }
      }
      
      public function get activeEffectID() : int
      {
         return this._activeEffectID;
      }
      
      public function set oneShotStatusID(param1:int) : void
      {
         this._oneShotStatusID = param1;
      }
      
      public function set oneShotStatusPriority(param1:int) : void
      {
         this._oneShotStatusPriority = param1;
      }
   }
}
