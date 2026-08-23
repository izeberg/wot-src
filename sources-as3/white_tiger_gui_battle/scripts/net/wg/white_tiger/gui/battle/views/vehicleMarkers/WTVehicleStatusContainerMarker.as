package net.wg.white_tiger.gui.battle.views.vehicleMarkers
{
   import flash.display.DisplayObject;
   import flash.events.Event;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.views.vehicleMarkers.VehicleStatusContainerMarker;
   import net.wg.gui.battle.views.vehicleMarkers.events.StatusAnimationEvent;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleAnimatedStatusBaseMarker;
   import net.wg.gui.battle.views.vehicleMarkers.statusMarkers.VehicleStunMarker;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_BATTLE_MARKER_STATES;
   import net.wg.white_tiger.gui.battle.views.vehicleMarkers.statusMarkers.WTUnionStrengthMarker;
   
   public class WTVehicleStatusContainerMarker extends VehicleStatusContainerMarker
   {
      
      private static const STUN_NAME_PREFIX:String = "wt_";
       
      
      public var unionStrengthMarker:WTUnionStrengthMarker = null;
      
      public var stunAreaMarker:VehicleStunMarker = null;
      
      public var silenceMarker:VehicleStunMarker = null;
      
      public function WTVehicleStatusContainerMarker()
      {
         super();
         setupMarker(WHITE_TIGER_BATTLE_MARKER_STATES.WT_UNION_STRENGTH_STATE,this.unionStrengthMarker);
         setupMarker(WHITE_TIGER_BATTLE_MARKER_STATES.WT_STUN_AREA_STATE,this.stunAreaMarker);
         setupMarker(WHITE_TIGER_BATTLE_MARKER_STATES.WT_STUN_AREA_MOD_A_STATE,this.stunAreaMarker);
         setupMarker(WHITE_TIGER_BATTLE_MARKER_STATES.WT_SILENCE_STATE,this.silenceMarker);
         setupMarker(WHITE_TIGER_BATTLE_MARKER_STATES.WT_INVISIBLE_STATE,statusMarker);
      }
      
      override public function setEffectColor(param1:String, param2:uint) : void
      {
         this.unionStrengthMarker.setEffectColor(param1,param2);
         this.stunAreaMarker.setEffectColor(param1,param2);
         this.silenceMarker.setEffectColor(param1,param2);
         super.setEffectColor(param1,param2);
         stunMarker.setEffectColor(STUN_NAME_PREFIX + param1,param2);
      }
      
      override public function setSecondString(param1:String) : void
      {
         this.stunAreaMarker.setSecondString(param1);
         this.silenceMarker.setSecondString(param1);
         super.setSecondString(param1);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.unionStrengthMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.stunAreaMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.silenceMarker.addEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.unionStrengthMarker.setupFrameEvents();
         this.stunAreaMarker.setupFrameEvents();
         this.silenceMarker.setupFrameEvents();
      }
      
      override protected function onDispose() : void
      {
         this.unionStrengthMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.unionStrengthMarker.dispose();
         this.unionStrengthMarker = null;
         this.stunAreaMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.stunAreaMarker.dispose();
         this.stunAreaMarker = null;
         this.silenceMarker.removeEventListener(StatusAnimationEvent.EVENT_HIDDEN,this.onStatusAnimationEventHiddenHandler);
         this.silenceMarker.dispose();
         this.silenceMarker = null;
         super.onDispose();
      }
      
      private function onStatusAnimationEventHiddenHandler(param1:StatusAnimationEvent) : void
      {
         var _loc2_:VehicleAnimatedStatusBaseMarker = null;
         if(param1.isOneShotAnimation)
         {
            oneShotStatusID = Values.DEFAULT_INT;
            oneShotStatusPriority = Values.DEFAULT_INT;
         }
         if(activeEffectID > Values.DEFAULT_INT)
         {
            _loc2_ = getMarker(activeEffectID);
            if(_loc2_)
            {
               _loc2_.setVisibility(true);
            }
         }
         else
         {
            DisplayObject(param1.currentTarget).x = Values.ZERO;
         }
         updateMarkersPositions();
         dispatchEvent(new Event(Event.COMPLETE));
      }
   }
}
