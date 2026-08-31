package net.wg.white_tiger.gui.battle.views.battleHints
{
   import net.wg.infrastructure.base.meta.IEventObjectivesMeta;
   import net.wg.infrastructure.base.meta.impl.EventObjectivesMeta;
   
   public class WhiteTigerObjectives extends EventObjectivesMeta implements IEventObjectivesMeta
   {
       
      
      public var txtMessage:WhiteTigerTextContainer = null;
      
      public function WhiteTigerObjectives()
      {
         super();
      }
      
      public function as_updateObjectives(param1:String) : void
      {
         this.visible = true;
         this.txtMessage.setText(param1);
      }
      
      public function as_hide() : void
      {
         this.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this.txtMessage.dispose();
         this.txtMessage = null;
         super.onDispose();
      }
   }
}
