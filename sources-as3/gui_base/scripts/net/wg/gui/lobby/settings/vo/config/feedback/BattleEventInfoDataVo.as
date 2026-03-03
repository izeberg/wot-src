package net.wg.gui.lobby.settings.vo.config.feedback
{
   import net.wg.gui.lobby.settings.config.ControlsFactory;
   import net.wg.gui.lobby.settings.vo.SettingsControlProp;
   import net.wg.gui.lobby.settings.vo.base.SettingsDataVo;
   
   public class BattleEventInfoDataVo extends SettingsDataVo
   {
       
      
      public var battleEventsShowInBattle:SettingsControlProp = null;
      
      public var battleEventsEventName:SettingsControlProp = null;
      
      public var battleEventsVehicleInfo:SettingsControlProp = null;
      
      public var battleEventsReceivedDamage:SettingsControlProp = null;
      
      public var battleEventsReceivedCrits:SettingsControlProp = null;
      
      public var battleEventsBlockedDamage:SettingsControlProp = null;
      
      public var battleEventsEnemyHpDamage:SettingsControlProp = null;
      
      public var battleEventsEnemyBurning:SettingsControlProp = null;
      
      public var battleEventsEnemyRamAttack:SettingsControlProp = null;
      
      public var battleEventsEnemyDetectionDamage:SettingsControlProp = null;
      
      public var battleEventsEnemyTrackDamage:SettingsControlProp = null;
      
      public var battleEventsEnemyDetection:SettingsControlProp = null;
      
      public var battleEventsEnemyKill:SettingsControlProp = null;
      
      public var battleEventsBaseCaptureDrop:SettingsControlProp = null;
      
      public var battleEventsBaseCapture:SettingsControlProp = null;
      
      public var battleEventsEnemyCriticalHit:SettingsControlProp = null;
      
      public var battleEventsEnemyWorldCollision:SettingsControlProp = null;
      
      public var battleEventsEnemyAssistStun:SettingsControlProp = null;
      
      public var battleEventsCrewPerks:SettingsControlProp = null;
      
      public var commander_eagleEye:SettingsControlProp = null;
      
      public var commander_emergency:SettingsControlProp = null;
      
      public var commander_tutor:SettingsControlProp = null;
      
      public var commander_coordination:SettingsControlProp = null;
      
      public var commander_holdLine:SettingsControlProp = null;
      
      public var commander_staySharp:SettingsControlProp = null;
      
      public var gunner_focus:SettingsControlProp = null;
      
      public var gunner_loneWolf:SettingsControlProp = null;
      
      public var driver_motorExpert:SettingsControlProp = null;
      
      public var driver_suspensionRepair:SettingsControlProp = null;
      
      public var driver_bulletproof:SettingsControlProp = null;
      
      public var loader_desperado:SettingsControlProp = null;
      
      public var loader_intuition:SettingsControlProp = null;
      
      public var loader_melee:SettingsControlProp = null;
      
      public var loader_secondChance:SettingsControlProp = null;
      
      public var radioman_sideBySide:SettingsControlProp = null;
      
      public var radioman_expert:SettingsControlProp = null;
      
      public var radioman_threatSearch:SettingsControlProp = null;
      
      public var damage:SettingsControlProp = null;
      
      public var battleEfficiency:SettingsControlProp = null;
      
      public var crewPerks:SettingsControlProp = null;
      
      public function BattleEventInfoDataVo()
      {
         super({
            "battleEventsReceivedDamage":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsReceivedCrits":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsShowInBattle":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsEnemyHpDamage":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsEnemyBurning":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsEnemyRamAttack":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsBlockedDamage":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsEnemyDetectionDamage":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsEnemyTrackDamage":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsEnemyDetection":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsEnemyKill":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsBaseCaptureDrop":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsBaseCapture":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsEnemyCriticalHit":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsEventName":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsVehicleInfo":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsEnemyWorldCollision":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsEnemyAssistStun":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "battleEventsCrewPerks":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "commander_eagleEye":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "commander_emergency":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "commander_tutor":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "commander_coordination":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "commander_holdLine":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "commander_staySharp":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "gunner_focus":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "gunner_loneWolf":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "driver_motorExpert":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "driver_suspensionRepair":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "driver_bulletproof":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "loader_desperado":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "loader_intuition":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "loader_melee":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "loader_secondChance":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "radioman_sideBySide":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "radioman_expert":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "radioman_threatSearch":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "damage":createControl(ControlsFactory.TYPE_CONTROLS_GROUP).build(),
            "battleEfficiency":createControl(ControlsFactory.TYPE_CONTROLS_GROUP).build(),
            "crewPerks":createControl(ControlsFactory.TYPE_CONTROLS_GROUP).build()
         });
      }
      
      override protected function onDispose() : void
      {
         this.battleEventsReceivedDamage = null;
         this.battleEventsReceivedCrits = null;
         this.battleEventsShowInBattle = null;
         this.battleEventsEnemyHpDamage = null;
         this.battleEventsEnemyBurning = null;
         this.battleEventsEnemyRamAttack = null;
         this.battleEventsBlockedDamage = null;
         this.battleEventsEnemyDetectionDamage = null;
         this.battleEventsEnemyTrackDamage = null;
         this.battleEventsEnemyDetection = null;
         this.battleEventsEnemyKill = null;
         this.battleEventsBaseCaptureDrop = null;
         this.battleEventsBaseCapture = null;
         this.battleEventsEnemyCriticalHit = null;
         this.battleEventsEventName = null;
         this.battleEventsVehicleInfo = null;
         this.battleEventsEnemyWorldCollision = null;
         this.battleEventsEnemyAssistStun = null;
         this.battleEventsCrewPerks = null;
         this.commander_eagleEye.dispose();
         this.commander_eagleEye = null;
         this.commander_emergency.dispose();
         this.commander_emergency = null;
         this.commander_tutor.dispose();
         this.commander_tutor = null;
         this.commander_coordination.dispose();
         this.commander_coordination = null;
         this.commander_holdLine.dispose();
         this.commander_holdLine = null;
         this.commander_staySharp.dispose();
         this.commander_staySharp = null;
         this.gunner_focus.dispose();
         this.gunner_focus = null;
         this.gunner_loneWolf.dispose();
         this.gunner_loneWolf = null;
         this.driver_motorExpert.dispose();
         this.driver_motorExpert = null;
         this.driver_suspensionRepair.dispose();
         this.driver_suspensionRepair = null;
         this.driver_bulletproof.dispose();
         this.driver_bulletproof = null;
         this.loader_desperado.dispose();
         this.loader_desperado = null;
         this.loader_intuition.dispose();
         this.loader_intuition = null;
         this.loader_melee.dispose();
         this.loader_melee = null;
         this.loader_secondChance.dispose();
         this.loader_secondChance = null;
         this.radioman_sideBySide.dispose();
         this.radioman_sideBySide = null;
         this.radioman_expert.dispose();
         this.radioman_expert = null;
         this.radioman_threatSearch.dispose();
         this.radioman_threatSearch = null;
         this.damage.dispose();
         this.damage = null;
         this.battleEfficiency.dispose();
         this.battleEfficiency = null;
         this.crewPerks.dispose();
         this.crewPerks = null;
         super.onDispose();
      }
   }
}
