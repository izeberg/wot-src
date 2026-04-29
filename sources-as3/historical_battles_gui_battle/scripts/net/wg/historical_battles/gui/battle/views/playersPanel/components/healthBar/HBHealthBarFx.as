package net.wg.historical_battles.gui.battle.views.playersPanel.components.healthBar
{
   import flash.display.MovieClip;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class HBHealthBarFx extends MovieClip implements IDisposable
   {
      
      private static const FX_FRAME:int = 2;
       
      
      public var bg:BattleAtlasSprite = null;
      
      private var _disposed:Boolean = false;
      
      public function HBHealthBarFx()
      {
         super();
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this.onDispose();
      }
      
      public function playAnim() : void
      {
         gotoAndPlay(FX_FRAME);
      }
      
      private function onDispose() : void
      {
         this.bg = null;
      }
      
      public function set isCurrentPlayer(param1:Boolean) : void
      {
         this.bg.imageName = !!param1 ? BATTLEATLAS.HB_HP_CURRENT_FX : BATTLEATLAS.HB_HP_ALLY_FX;
      }
      
      public function set isBlindEnabled(param1:Boolean) : void
      {
         this.bg.imageName = !!param1 ? BATTLEATLAS.HB_HP_ENEMY_BLIND_FX : BATTLEATLAS.HB_HP_ENEMY_FX;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
   }
}
