package net.wg.white_tiger.gui.lobby.settings
{
   import net.wg.white_tiger.gui.lobby.settings.components.SettingLabel;
   import net.wg.white_tiger.infrastructure.base.meta.IWhiteTigerSettingsWindowMeta;
   import net.wg.white_tiger.infrastructure.base.meta.impl.WhiteTigerSettingsWindowMeta;
   
   public class WhiteTigerSettingsWindow extends WhiteTigerSettingsWindowMeta implements IWhiteTigerSettingsWindowMeta
   {
       
      
      public var eventDisableLabel:SettingLabel = null;
      
      public function WhiteTigerSettingsWindow()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.eventDisableLabel.dispose();
         this.eventDisableLabel = null;
         super.onDispose();
      }
      
      public function as_setIsEvent(param1:Boolean) : void
      {
         this.eventDisableLabel.visible = param1;
      }
   }
}
