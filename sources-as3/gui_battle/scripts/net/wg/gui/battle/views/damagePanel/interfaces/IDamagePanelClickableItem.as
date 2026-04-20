package net.wg.gui.battle.views.damagePanel.interfaces
{
   import net.wg.gui.battle.views.damagePanel.components.DamagePanelItemClickArea;
   
   public interface IDamagePanelClickableItem extends IAssetCreator
   {
       
      
      function showDestroyed(param1:Boolean) : void;
      
      function get mouseEventHitElement() : DamagePanelItemClickArea;
   }
}
