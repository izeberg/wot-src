package net.wg.frontline.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.views.BaseBattlePage;
   
   public class FrontlineBattlePageMeta extends BaseBattlePage
   {
       
      
      public var onDeactivateRadialMenu:Function;
      
      public function FrontlineBattlePageMeta()
      {
         super();
      }
      
      public function onDeactivateRadialMenuS() : void
      {
         App.utils.asserter.assertNotNull(this.onDeactivateRadialMenu,"onDeactivateRadialMenu" + Errors.CANT_NULL);
         this.onDeactivateRadialMenu();
      }
   }
}
