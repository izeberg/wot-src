package net.wg.gui.lobby.hangar
{
   import net.wg.data.constants.generated.HANGAR_CONSTS;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class HangarContentHelper implements IDisposable
   {
       
      
      private var _hangar:Hangar;
      
      private var _disposed:Boolean = false;
      
      public function HangarContentHelper(param1:Hangar)
      {
         super();
         this._hangar = param1;
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this._hangar = null;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function updateHideComponents(param1:Array) : void
      {
         var _loc2_:String = null;
         for each(_loc2_ in param1)
         {
            switch(_loc2_)
            {
               case HANGAR_CONSTS.CREW:
                  this._hangar.crewPanelInject.visible = false;
                  break;
               case HANGAR_CONSTS.AMMUNITION:
                  this._hangar.ammunitionPanel.visible = false;
                  break;
               case HANGAR_CONSTS.AMMUNITION_INJECT:
                  this._hangar.ammunitionPanelInject.visible = false;
                  break;
               case HANGAR_CONSTS.CAROUSEL:
                  this._hangar.carouselVisible = false;
                  break;
               case HANGAR_CONSTS.SWITCH_MODE:
                  this._hangar.switchModePanel.visible = false;
                  break;
               case HANGAR_CONSTS.VEHICLE_PARAMETERS:
                  this._hangar.params.visible = false;
                  break;
               case HANGAR_CONSTS.HEADER:
                  this._hangar.header.visible = false;
                  break;
               case HANGAR_CONSTS.VEHICLE_RESEARCH:
                  this._hangar.vehResearchBG.visible = false;
                  this._hangar.vehResearchPanel.visible = false;
                  break;
               case HANGAR_CONSTS.ALERT_MESSAGE:
                  this._hangar.removeAlertMessage();
                  break;
               case HANGAR_CONSTS.PRESTIGE_WIDGET:
                  this._hangar.removePrestigeWidget();
                  break;
            }
         }
      }
      
      public function updateShowComponents(param1:Array) : void
      {
         var _loc2_:String = null;
         for each(_loc2_ in param1)
         {
            switch(_loc2_)
            {
               case HANGAR_CONSTS.CREW:
                  this._hangar.crewPanelInject.visible = true;
                  break;
               case HANGAR_CONSTS.AMMUNITION:
                  this._hangar.ammunitionPanel.visible = true;
                  break;
               case HANGAR_CONSTS.AMMUNITION_INJECT:
                  this._hangar.ammunitionPanelInject.visible = true;
                  break;
               case HANGAR_CONSTS.CAROUSEL:
                  this._hangar.carouselVisible = true;
                  break;
               case HANGAR_CONSTS.SWITCH_MODE:
                  this._hangar.switchModePanel.visible = true;
                  break;
               case HANGAR_CONSTS.VEHICLE_PARAMETERS:
                  this._hangar.params.visible = true;
                  break;
               case HANGAR_CONSTS.HEADER:
                  this._hangar.header.visible = true;
                  break;
               case HANGAR_CONSTS.VEHICLE_RESEARCH:
                  this._hangar.vehResearchBG.visible = true;
                  this._hangar.vehResearchPanel.visible = true;
                  break;
               case HANGAR_CONSTS.ALERT_MESSAGE:
                  this._hangar.addAlertMessage();
                  break;
               case HANGAR_CONSTS.PRESTIGE_WIDGET:
                  this._hangar.addPrestigeWidget();
                  break;
            }
         }
      }
   }
}
