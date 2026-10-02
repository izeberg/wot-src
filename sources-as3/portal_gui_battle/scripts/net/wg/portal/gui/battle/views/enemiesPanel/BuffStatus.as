package net.wg.portal.gui.battle.views.enemiesPanel
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.gui.battle.components.BattleDisplayable;
   
   public class BuffStatus extends BattleDisplayable
   {
      
      private static const BUFF_ATTENTION_ICON_OFFSET_X:uint = 18;
       
      
      public var buffAttentionIcon:MovieClip = null;
      
      public var buffStatusTf:TextField = null;
      
      public var buffStatusBg:MovieClip = null;
      
      public function BuffStatus()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.buffAttentionIcon = null;
         this.buffStatusTf = null;
         this.buffStatusBg = null;
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.buffStatusTf.text = PORTAL_EVENT.BATTLE_STATUS_BUFF;
         this.buffAttentionIcon.x = width - this.buffStatusTf.textWidth - this.buffAttentionIcon.width - BUFF_ATTENTION_ICON_OFFSET_X | 0;
      }
   }
}
