package net.wg.white_tiger.gui.battle.views.battleHints
{
   import flash.display.Sprite;
   import net.wg.infrastructure.base.meta.IBattleHintMeta;
   import net.wg.white_tiger.gui.battle.VO.WhiteTigerBattleHintVO;
   import net.wg.white_tiger.infrastructure.base.meta.impl.WhiteTigerBattleHintMeta;
   
   public class WhiteTigerBattleHint extends WhiteTigerBattleHintMeta implements IBattleHintMeta
   {
       
      
      public var hintContainer:WhiteTigerInfoContainer = null;
      
      private var _container:Sprite;
      
      public const HINT_DEFAULT_Y_POSITION:int = 140;
      
      public const HINT_CONTAINER_Y_OFFSET:int = 12;
      
      public function WhiteTigerBattleHint()
      {
         this._container = new Sprite();
         super();
         addChild(this._container);
         this._container.addChild(this.hintContainer);
      }
      
      override protected function onDispose() : void
      {
         this._container.removeChild(this.hintContainer);
         removeChild(this._container);
         this._container = null;
         this.hintContainer.dispose();
         this.hintContainer = null;
         super.onDispose();
      }
      
      public function as_hideHint() : void
      {
         this.hintContainer.hideHint();
      }
      
      override protected function showHint(param1:WhiteTigerBattleHintVO) : void
      {
         this.hintContainer.showHint(param1);
      }
      
      public function updatePositionY(param1:Number) : void
      {
         this.y = param1;
      }
      
      public function as_cancelFadeOut() : void
      {
         this.hintContainer.hideHintImmediately();
      }
      
      public function updateStage(param1:Number, param2:Number) : void
      {
         this.hintContainer.updateStage(param1,param2);
         this._container.x = param1 >> 1;
      }
   }
}
