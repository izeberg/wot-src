package net.wg.white_tiger.gui.battle.views.vehicleMarkers
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.geom.ColorTransform;
   import flash.text.TextField;
   import net.wg.gui.battle.views.vehicleMarkers.HealthBarAnimatedPart;
   import net.wg.gui.battle.views.vehicleMarkers.VehicleMarker;
   import net.wg.gui.battle.views.vehicleMarkers.VehicleMarkersConstants;
   
   public class WTVehicleMarker extends VehicleMarker
   {
      
      private static const VEHICLE_MARKER_TOP_OFFSET:Number = 7;
      
      private static const PLASMA_DAMAGE:String = "plasmaDamage";
      
      private static const PLASMA_HIT_LABEL_LEFT_OFFSET:int = 2;
      
      private static const PLASMA_ICON_LEFT_OFFSET:int = 0;
      
      private static const PLASMA_ICON_TOP_OFFSET:int = 2;
      
      private static const PLASMA_ICON_RIGHT_OFFSET:int = 5;
      
      private static const HIT_EXPLOSION_LABEL_LEFT_OFFSET:int = 15;
      
      private static const CRITICAL_HIT_LABEL_LEFT_OFFSET:int = 15;
      
      private static const HIT_LABEL_RIGHT_OFFSET:int = 2;
      
      private static const ABILITY_DURATION_FIELD_OFFSET:int = -5;
       
      
      public var abilityDurationField:TextField = null;
      
      public var plasmaBuffMc:MovieClip = null;
      
      public var plasmaHitDamage:PlasmaDamageAnimatedLabel = null;
      
      private var _plasmaDamage:Number = 0;
      
      private var _hitDamage:int = 0;
      
      public function WTVehicleMarker()
      {
         super();
         this.plasmaBuffMc.visible = false;
      }
      
      override public function activateHover(param1:Boolean) : void
      {
      }
      
      override public function setDistance(param1:String) : void
      {
      }
      
      override public function setDistanceVisibility(param1:Boolean) : void
      {
      }
      
      override public function setVehicleInfo(param1:String, param2:String, param3:String, param4:int, param5:String, param6:String, param7:String, param8:String, param9:int, param10:String, param11:Boolean, param12:int, param13:String, param14:String = "", param15:int = 0) : void
      {
         super.setVehicleInfo(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,param11,param12,param13,param14,param15);
         super.setDistanceVisibility(false);
      }
      
      override public function showStatTrackMarker(param1:String, param2:String, param3:Number = 1, param4:Boolean = false) : void
      {
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.plasmaHitDamage.addEventListener(HealthBarAnimatedPart.SHOW,this.onHitSplashShowHandler);
         this.plasmaHitDamage.addEventListener(HealthBarAnimatedPart.HIDE,this.onHitSplashHideHandler);
         hitLabel.addEventListener(HealthBarAnimatedPart.HIDE,this.onHitLabelHideHandler);
      }
      
      override protected function onDispose() : void
      {
         this.abilityDurationField = null;
         this.plasmaBuffMc = null;
         this.plasmaHitDamage.removeEventListener(HealthBarAnimatedPart.SHOW,this.onHitSplashShowHandler);
         this.plasmaHitDamage.removeEventListener(HealthBarAnimatedPart.HIDE,this.onHitSplashHideHandler);
         if(this.plasmaHitDamage != null)
         {
            this.plasmaHitDamage.dispose();
         }
         this.plasmaHitDamage = null;
         hitLabel.removeEventListener(HealthBarAnimatedPart.HIDE,this.onHitLabelHideHandler);
         super.onDispose();
      }
      
      override protected function updateHitLayout() : void
      {
         var _loc1_:Boolean = hitLabel.visible && hitLabel.isActive();
         var _loc2_:int = !!_loc1_ ? int(hitLabel.damageLabel.textWidth + HIT_LABEL_RIGHT_OFFSET) : int(0);
         var _loc3_:DamageLabel = DamageLabel(this.plasmaHitDamage.damageLabel);
         this.plasmaHitDamage.x = hitLabel.x + _loc2_ + PLASMA_HIT_LABEL_LEFT_OFFSET | 0;
         var _loc4_:Boolean = this.plasmaHitDamage.visible && this.plasmaHitDamage.isActive();
         if(this.plasmaHitDamage.plasmaIcon)
         {
            this.plasmaHitDamage.plasmaIcon.y = PLASMA_ICON_TOP_OFFSET;
            this.plasmaHitDamage.plasmaIcon.x = _loc3_.plasmaDamage.textWidth + PLASMA_ICON_LEFT_OFFSET | 0;
         }
         var _loc5_:int = !!_loc4_ ? int(_loc3_.plasmaDamage.textWidth + this.plasmaHitDamage.plasmaIcon.width + PLASMA_ICON_RIGHT_OFFSET) : int(0);
         hitExplosion.x = hitLabel.x + _loc2_ + _loc5_ + HIT_EXPLOSION_LABEL_LEFT_OFFSET | 0;
         criticalHitLabel.x = hitExplosion.x + CRITICAL_HIT_LABEL_LEFT_OFFSET | 0;
      }
      
      override protected function applyColor() : void
      {
         var _loc1_:ColorTransform = null;
         super.applyColor();
         if(isObserver)
         {
            _loc1_ = vmManager.getTransform(markerSchemeName);
            this.plasmaHitDamage.transform.colorTransform = _loc1_;
         }
      }
      
      override protected function prepareOffsets() : void
      {
         offsets.push(ABILITY_DURATION_FIELD_OFFSET);
      }
      
      override protected function showHitLabelAnim(param1:int, param2:String) : void
      {
         var _loc3_:Boolean = this._hitDamage * param1 < 0;
         if(_loc3_)
         {
            hitLabel.tweenState = VehicleMarkersConstants.HB_ANIMATED_INACTIVE_STATE;
         }
         hitLabel.damage(param1,param2);
         hitLabel.playShowTween();
         this._hitDamage = param1;
      }
      
      public function setAbilityDurationValue(param1:String) : void
      {
         this.abilityDurationField.text = param1;
      }
      
      public function setPlasmaBuffValue(param1:Number) : void
      {
         this.plasmaBuffMc.gotoAndStop(param1 + 1);
      }
      
      public function showPlasmaBuff(param1:Boolean) : void
      {
         if(this.plasmaBuffMc.visible == param1)
         {
            return;
         }
         marker.y += VEHICLE_MARKER_TOP_OFFSET;
         this.plasmaBuffMc.visible = param1;
      }
      
      public function showPlasmaDamage(param1:Number) : void
      {
         if(this.plasmaHitDamage.tweenState != VehicleMarkersConstants.HB_ANIMATED_INACTIVE_STATE && this.plasmaHitDamage.tweenState != VehicleMarkersConstants.HB_ANIMATED_IMITATION_STATE)
         {
            this._plasmaDamage += param1;
         }
         else
         {
            this._plasmaDamage = param1;
         }
         this.plasmaHitDamage.setLabel("(" + this._plasmaDamage.toString(),PLASMA_DAMAGE);
         this.updateHitLayout();
         this.plasmaHitDamage.playShowTween();
         this.plasmaHitDamage.plasmaIcon.gotoAndPlay(this.plasmaHitDamage.tweenState);
      }
      
      private function onHitSplashShowHandler(param1:Event) : void
      {
         this.plasmaHitDamage.visible = true;
      }
      
      private function onHitSplashHideHandler(param1:Event) : void
      {
         this.plasmaHitDamage.plasmaIcon.gotoAndPlay(1);
         this.plasmaHitDamage.visible = false;
         this._plasmaDamage = 0;
      }
      
      private function onHitLabelHideHandler(param1:Event) : void
      {
         this._hitDamage = 0;
      }
   }
}
