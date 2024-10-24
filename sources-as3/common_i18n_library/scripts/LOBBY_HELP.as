package
{
   public class LOBBY_HELP
   {
      
      public static const HEADER_SETTINGS_BUTTON:String = "#lobby_help:header/settings-button";
      
      public static const HEADER_ACCOUNT_BUTTON:String = "#lobby_help:header/account-button";
      
      public static const HEADER_PREMIUM_BUTTON:String = "#lobby_help:header/premium-button";
      
      public static const HEADER_WOT_PLUS_BUTTON:String = "#lobby_help:header/wot-plus-button";
      
      public static const HEADER_SQUAD_BUTTON:String = "#lobby_help:header/squad-button";
      
      public static const HEADER_BATTLETYPE_BUTTON:String = "#lobby_help:header/battleType-button";
      
      public static const HEADER_FINANCE_BLOCK:String = "#lobby_help:header/finance-block";
      
      public static const HEADER_PERSONAL_RESERVES:String = "#lobby_help:header/personal-reserves";
      
      public static const VEHICLE_COMPARE:String = "#lobby_help:vehicle/compare";
      
      public static const CHAT_SERVICE_CHANNEL:String = "#lobby_help:chat/service-channel";
      
      public static const CHAT_CONTACTS_CHANNEL:String = "#lobby_help:chat/contacts-channel";
      
      public static const CHANNELCAROUSEL_CHANNELS:String = "#lobby_help:channelCarousel/channels";
      
      public static const HANGAR_AMMUNITIONPANEL_MAIN:String = "#lobby_help:hangar/ammunitionPanel/main";
      
      public static const HANGAR_CREW:String = "#lobby_help:hangar/crew";
      
      public static const HANGAR_CREWOPERATIONS:String = "#lobby_help:hangar/crewOperations";
      
      public static const HANGAR_VEHICLE_PARAMETERS:String = "#lobby_help:hangar/vehicle-parameters";
      
      public static const HANGAR_VEHICLE_CAROUSEL:String = "#lobby_help:hangar/vehicle-carousel";
      
      public static const HANGAR_QUESTSCONTROL:String = "#lobby_help:hangar/questsControl";
      
      public static const HANGAR_VEHRESEARCHPANEL:String = "#lobby_help:hangar/vehResearchPanel";
      
      public static const HANGAR_VEHFILTERS:String = "#lobby_help:hangar/vehFilters";
      
      public static const HANGAR_HEADER_QUESTS:String = "#lobby_help:hangar/header/quests";
      
      public static const HANGAR_HEADER_VEHICLE:String = "#lobby_help:hangar/header/vehicle";
      
      public static const HANGAR_SESSIONSTATS:String = "#lobby_help:hangar/sessionStats";
      
      public static const HANGAR_PRESTIGE:String = "#lobby_help:hangar/prestige";
      
      public static const HANGAR_AMMUNITIONPANEL_ENUM:Array = [HANGAR_AMMUNITIONPANEL_MAIN];
       
      
      public function LOBBY_HELP()
      {
         super();
      }
      
      public static function getAmmunitionPanelHelpMsg(param1:String) : String
      {
         var _loc2_:String = "#lobby_help:" + "hangar/ammunitionPanel/" + param1;
         if(HANGAR_AMMUNITIONPANEL_ENUM.indexOf(_loc2_) == -1)
         {
            DebugUtils.LOG_WARNING("[getAmmunitionPanelHelpMsg]:locale key \"" + _loc2_ + "\" was not found");
            return null;
         }
         return _loc2_;
      }
   }
}
