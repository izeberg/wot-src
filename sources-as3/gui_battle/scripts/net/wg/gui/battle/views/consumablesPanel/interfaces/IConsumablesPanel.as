package net.wg.gui.battle.views.consumablesPanel.interfaces
{
   import net.wg.gui.battle.components.buttons.interfaces.IClickButtonHandler;
   import net.wg.gui.battle.components.buttons.interfaces.IRollOutButtonHandler;
   import net.wg.gui.battle.components.buttons.interfaces.IRollOverButtonHandler;
   import net.wg.infrastructure.base.meta.IConsumablesPanelMeta;
   
   public interface IConsumablesPanel extends IConsumablesPanelMeta, IClickButtonHandler, IRollOverButtonHandler, IRollOutButtonHandler
   {
       
   }
}
