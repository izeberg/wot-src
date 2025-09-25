package net.wg.gui.lobby.settings.vo.config.aim
{
   import net.wg.gui.lobby.settings.config.ControlsFactory;
   import net.wg.gui.lobby.settings.vo.SettingsControlProp;
   import net.wg.gui.lobby.settings.vo.base.SettingsDataVo;
   
   public class AimSettingsArmorFlashlightDataVo extends SettingsDataVo
   {
       
      
      public var armorFlashlightEnabled:SettingsControlProp = null;
      
      public var armorFlashlightColorSchema:SettingsControlProp = null;
      
      public var armorFlashlightOpacity:SettingsControlProp = null;
      
      public var armorFlashlightFill:SettingsControlProp = null;
      
      public var armorFlashlightResolutionScaling:SettingsControlProp = null;
      
      public function AimSettingsArmorFlashlightDataVo()
      {
         super({
            "armorFlashlightEnabled":createControl(ControlsFactory.TYPE_CHECKBOX).build(),
            "armorFlashlightColorSchema":createControl(ControlsFactory.TYPE_BUTTON_BAR).build(),
            "armorFlashlightOpacity":createControl(ControlsFactory.TYPE_SLIDER).build(),
            "armorFlashlightFill":createControl(ControlsFactory.TYPE_BUTTON_BAR).build(),
            "armorFlashlightResolutionScaling":createControl(ControlsFactory.TYPE_DROPDOWN).build()
         });
      }
      
      override protected function onDispose() : void
      {
         this.armorFlashlightEnabled = null;
         this.armorFlashlightColorSchema = null;
         this.armorFlashlightOpacity = null;
         this.armorFlashlightFill = null;
         this.armorFlashlightResolutionScaling = null;
         super.onDispose();
      }
   }
}
