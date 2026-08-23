package net.wg.gui.lobby.settings.feedback.ribbons
{
   import flash.events.Event;
   import flash.utils.Dictionary;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.VehicleTypes;
   import net.wg.data.constants.generated.BATTLE_EFFICIENCY_TYPES;
   import net.wg.gui.components.ribbon.data.RibbonSettingsLobby;
   import net.wg.gui.lobby.settings.feedback.ribbons.data.RibbonItemData;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.events.ColorSchemeEvent;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import net.wg.infrastructure.managers.IColorSchemeManager;
   
   public class SettingsRibbonContainer extends UIComponentEx
   {
      
      private static const E100:String = "#germany_vehicles:E-100";
      
      private static const ITEM_STEP_Y:int = 30;
      
      private static const FIRST_ITEM_OFFSET:int = 8;
      
      private static const MAX_VISIBLE_ITEMS:int = 15;
       
      
      private var _itemsMap:Dictionary = null;
      
      private var _itemsData:Vector.<RibbonItemData> = null;
      
      private var _colorMgr:IColorSchemeManager = null;
      
      public function SettingsRibbonContainer()
      {
         var _loc2_:SettingsRibbonItem = null;
         var _loc3_:RibbonItemData = null;
         var _loc5_:RibbonSettingsLobby = null;
         super();
         this._itemsData = new <RibbonItemData>[new RibbonItemData(BATTLE_EFFICIENCY_TYPES.RECEIVED_DAMAGE,SETTINGS.FEEDBACK_TAB_BATTLEEVENTS_RECEIVEDDAMAGE,SETTINGS.FEEDBACK_TAB_RIBBONS_DAMAGEVALUE,E100,VehicleTypes.HEAVY_TANK),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.RECEIVED_CRITS,INGAME_GUI.EFFICIENCYRIBBONS_RECEIVEDCRITS,SETTINGS.FEEDBACK_TAB_RIBBONS_CRITVALUE,E100,VehicleTypes.HEAVY_TANK),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.ARMOR,INGAME_GUI.EFFICIENCYRIBBONS_ARMOR,SETTINGS.FEEDBACK_TAB_RIBBONS_ARMORVALUE,E100,VehicleTypes.HEAVY_TANK),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.DEFENCE,INGAME_GUI.EFFICIENCYRIBBONS_DEFENCE,SETTINGS.FEEDBACK_TAB_RIBBONS_DEFENCEVALUE),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.CAPTURE,INGAME_GUI.EFFICIENCYRIBBONS_CAPTURE,SETTINGS.FEEDBACK_TAB_RIBBONS_CAPTUREVALUE),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.DETECTION,INGAME_GUI.EFFICIENCYRIBBONS_SPOTTED,Values.EMPTY_STR),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.RAM,INGAME_GUI.EFFICIENCYRIBBONS_RAM,SETTINGS.FEEDBACK_TAB_RIBBONS_RAMVALUE,E100,VehicleTypes.HEAVY_TANK),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.DESTRUCTION,INGAME_GUI.EFFICIENCYRIBBONS_KILL,Values.EMPTY_STR,E100,VehicleTypes.HEAVY_TANK),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.ASSIST_TRACK,INGAME_GUI.EFFICIENCYRIBBONS_ASSISTTRACK,SETTINGS.FEEDBACK_TAB_RIBBONS_ASSISTTRACKVALUE,E100,VehicleTypes.HEAVY_TANK),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.CRITS,INGAME_GUI.EFFICIENCYRIBBONS_CRITS,Values.EMPTY_STR,E100,VehicleTypes.HEAVY_TANK),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.DAMAGE,INGAME_GUI.EFFICIENCYRIBBONS_DAMAGE,SETTINGS.FEEDBACK_TAB_RIBBONS_DAMAGEVALUE,E100,VehicleTypes.HEAVY_TANK),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.WORLD_COLLISION,INGAME_GUI.EFFICIENCYRIBBONS_WORLDCOLLISION,SETTINGS.FEEDBACK_TAB_RIBBONS_DAMAGEVALUE,E100,VehicleTypes.HEAVY_TANK),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.ASSIST_SPOT,INGAME_GUI.EFFICIENCYRIBBONS_ASSISTSPOT,SETTINGS.FEEDBACK_TAB_RIBBONS_ASSISTSPOTVALUE,E100,VehicleTypes.HEAVY_TANK),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.ASSIST_STUN,INGAME_GUI.EFFICIENCYRIBBONS_ASSISTSTUN,SETTINGS.FEEDBACK_TAB_RIBBONS_ASSISTSTUN,E100,VehicleTypes.HEAVY_TANK),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.BURN,INGAME_GUI.EFFICIENCYRIBBONS_BURN,SETTINGS.FEEDBACK_TAB_RIBBONS_BURNVALUE,E100,VehicleTypes.HEAVY_TANK),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.COMMANDER_EAGLE_EYE,CREW_PERKS.COMMANDER_EAGLEEYE_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.COMMANDER_EMERGENCY,CREW_PERKS.COMMANDER_EMERGENCY_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.COMMANDER_TUTOR,CREW_PERKS.COMMANDER_TUTOR_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.COMMANDER_COORDINATION,CREW_PERKS.COMMANDER_COORDINATION_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.COMMANDER_HOLD_LINE,CREW_PERKS.COMMANDER_HOLDLINE_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.COMMANDER_STAY_SHARP,CREW_PERKS.COMMANDER_STAYSHARP_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.GUNNER_FOCUS,CREW_PERKS.GUNNER_FOCUS_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.GUNNER_LONE_WOLF,CREW_PERKS.GUNNER_LONEWOLF_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.DRIVER_MOTOR_EXPERT,CREW_PERKS.DRIVER_MOTOREXPERT_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.DRIVER_SUSPENSION_REPAIR,CREW_PERKS.DRIVER_SUSPENSIONREPAIR_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.DRIVER_BULLETPROOF,CREW_PERKS.DRIVER_BULLETPROOF_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.LOADER_DESPERADO,CREW_PERKS.LOADER_DESPERADO_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.LOADER_INTUITION,CREW_PERKS.LOADER_INTUITION_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.LOADER_MELEE,CREW_PERKS.LOADER_MELEE_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.LOADER_SECOND_CHANCE,CREW_PERKS.LOADER_SECONDCHANCE_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.RADIOMAN_SIDE_BY_SIDE,CREW_PERKS.RADIOMAN_SIDEBYSIDE_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.RADIOMAN_EXPERT,CREW_PERKS.RADIOMAN_EXPERT_NAME),new RibbonItemData(BATTLE_EFFICIENCY_TYPES.RADIOMAN_THREAT_SEARCH,CREW_PERKS.RADIOMAN_THREATSEARCH_NAME)];
         this._itemsMap = new Dictionary();
         var _loc1_:int = this._itemsData.length;
         var _loc4_:int = 0;
         while(_loc4_ < _loc1_)
         {
            _loc3_ = this._itemsData[_loc4_];
            _loc5_ = new RibbonSettingsLobby(_loc3_.ribbonType,_loc3_.text);
            _loc2_ = new SettingsRibbonItem(_loc5_);
            _loc2_.y = FIRST_ITEM_OFFSET + ITEM_STEP_Y * _loc4_;
            this.addChild(_loc2_);
            _loc2_.setData(_loc3_.vehType,_loc3_.vehName,_loc3_.value);
            this._itemsMap[_loc3_.ribbonType] = _loc2_;
            _loc4_++;
         }
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._colorMgr = App.colorSchemeMgr;
         this._colorMgr.addEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorMgrSchemasUpdateHandler);
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:IDisposable = null;
         this._itemsData.splice(0,this._itemsData.length);
         this._itemsData = null;
         for each(_loc1_ in this._itemsMap)
         {
            _loc1_.dispose();
         }
         App.utils.data.cleanupDynamicObject(this._itemsMap);
         this._itemsMap = null;
         this._colorMgr.removeEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onColorMgrSchemasUpdateHandler);
         this._colorMgr = null;
         super.onDispose();
      }
      
      public function redraw() : void
      {
         var _loc1_:int = this._itemsData.length;
         var _loc2_:int = 0;
         var _loc3_:String = null;
         var _loc4_:SettingsRibbonItem = null;
         var _loc5_:int = FIRST_ITEM_OFFSET;
         if(this.numChildren < MAX_VISIBLE_ITEMS)
         {
            _loc5_ += (MAX_VISIBLE_ITEMS - this.numChildren) * ITEM_STEP_Y;
         }
         var _loc6_:int = 0;
         while(_loc6_ < _loc1_)
         {
            _loc3_ = this._itemsData[_loc6_].ribbonType;
            _loc4_ = this._itemsMap[_loc3_];
            if(_loc4_.parent)
            {
               _loc4_.y = _loc5_ + _loc2_ * ITEM_STEP_Y;
               _loc2_++;
            }
            _loc6_++;
         }
         setSize(actualWidth,actualHeight - 8);
         dispatchEvent(new Event(Event.RESIZE));
      }
      
      public function updateItemVisible(param1:String, param2:Boolean) : void
      {
         var _loc3_:SettingsRibbonItem = this._itemsMap[param1];
         if(param2 && !_loc3_.parent)
         {
            this.addChild(_loc3_);
         }
         else if(!param2 && _loc3_.parent)
         {
            this.removeChild(_loc3_);
         }
      }
      
      public function updateSettings(param1:Boolean, param2:Boolean) : void
      {
         var _loc3_:SettingsRibbonItem = null;
         for each(_loc3_ in this._itemsMap)
         {
            _loc3_.updateSettings(param1,param2);
         }
      }
      
      private function onColorMgrSchemasUpdateHandler(param1:ColorSchemeEvent) : void
      {
         var _loc2_:SettingsRibbonItem = null;
         for each(_loc2_ in this._itemsMap)
         {
            _loc2_.update();
         }
      }
   }
}
