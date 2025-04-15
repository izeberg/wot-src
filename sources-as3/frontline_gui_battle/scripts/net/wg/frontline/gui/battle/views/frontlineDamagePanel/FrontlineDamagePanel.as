package net.wg.frontline.gui.battle.views.frontlineDamagePanel
{
   import net.wg.frontline.gui.battle.views.frontlineDamagePanel.components.GeneralBonus;
   import net.wg.frontline.infrastructure.base.meta.IFrontlineDamagePanelMeta;
   import net.wg.frontline.infrastructure.base.meta.impl.FrontlineDamagePanelMeta;
   
   public class FrontlineDamagePanel extends FrontlineDamagePanelMeta implements IFrontlineDamagePanelMeta
   {
      
      private static const ZERO_BONUS:int = 0;
       
      
      public var generalBonus:GeneralBonus = null;
      
      public function FrontlineDamagePanel()
      {
         super();
         this.generalBonus.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this.generalBonus.dispose();
         this.generalBonus = null;
         super.onDispose();
      }
      
      public function as_setGeneralBonus(param1:Number) : void
      {
         if(param1 > ZERO_BONUS)
         {
            this.generalBonus.visible = true;
            this.generalBonus.bonusValue = param1;
         }
      }
   }
}
