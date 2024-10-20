package net.wg.gui.battle.views.epicDamagePanel
{
   import net.wg.gui.battle.views.damagePanel.DamagePanel;
   import net.wg.gui.battle.views.epicDamagePanel.components.GeneralBonus;
   import net.wg.infrastructure.base.meta.IEpicDamagePanelMeta;
   
   public class EpicDamagePanel extends DamagePanel implements IEpicDamagePanelMeta
   {
      
      private static const ZERO_BONUS:int = 0;
       
      
      public var generalBonus:GeneralBonus = null;
      
      public function EpicDamagePanel()
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
