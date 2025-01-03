package net.wg.gui.battle.views.debugPanel
{
   import flash.text.TextField;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.infrastructure.base.meta.IDebugPanelMeta;
   import net.wg.infrastructure.base.meta.impl.DebugPanelMeta;
   import scaleform.gfx.TextFieldEx;
   
   public class DebugPanel extends DebugPanelMeta implements IDebugPanelMeta
   {
      
      private static const REPLAY_POS_X:int = 23;
       
      
      public var fpsTF:TextField = null;
      
      public var pingTF:TextField = null;
      
      public var lagOnlineSpr:BattleAtlasSprite = null;
      
      public var lagOfflineSpr:BattleAtlasSprite = null;
      
      public var bg:BattleAtlasSprite = null;
      
      public function DebugPanel()
      {
         super();
         TextFieldEx.setNoTranslate(this.fpsTF,true);
         TextFieldEx.setNoTranslate(this.pingTF,true);
         this.lagOnlineSpr.imageName = BATTLEATLAS.DEBUG_ON;
         this.lagOfflineSpr.imageName = BATTLEATLAS.DEBUG_OFF;
         this.bg.imageName = BATTLEATLAS.DEBUG_BG;
      }
      
      override protected function onDispose() : void
      {
         this.lagOnlineSpr = null;
         this.lagOfflineSpr = null;
         this.bg = null;
         this.fpsTF = null;
         this.pingTF = null;
         super.onDispose();
      }
      
      public function as_initReplay() : void
      {
         x = REPLAY_POS_X;
      }
      
      public function as_updateAll(param1:int, param2:int, param3:Boolean) : void
      {
         this.pingTF.text = param1.toString();
         this.fpsTF.text = param2.toString();
         this.lagOnlineSpr.visible = !param3;
         this.lagOfflineSpr.visible = param3;
      }
      
      public function as_updateFps(param1:int) : void
      {
         this.fpsTF.text = param1.toString();
      }
      
      public function as_updatePing(param1:int) : void
      {
         this.pingTF.text = param1.toString();
      }
      
      public function as_updatePingFPS(param1:int, param2:int) : void
      {
         this.pingTF.text = param1.toString();
         this.fpsTF.text = param2.toString();
      }
      
      public function as_updateReplay(param1:int, param2:int, param3:Boolean, param4:int) : void
      {
         if(param1 >= 0)
         {
            this.pingTF.text = param1.toString();
         }
         if(param4 > 0)
         {
            this.fpsTF.text = param4.toString() + "(" + param2.toString() + ")";
         }
         if(this.lagOfflineSpr.visible != param3)
         {
            this.lagOnlineSpr.visible = !param3;
            this.lagOfflineSpr.visible = param3;
         }
      }
   }
}
