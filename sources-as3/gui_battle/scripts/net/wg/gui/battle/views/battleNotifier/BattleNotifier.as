package net.wg.gui.battle.views.battleNotifier
{
   import net.wg.infrastructure.base.meta.IBattleNotifierMeta;
   import net.wg.infrastructure.base.meta.impl.BattleNotifierMeta;
   import net.wg.infrastructure.interfaces.entity.IDisplayableComponent;
   
   public class BattleNotifier extends BattleNotifierMeta implements IBattleNotifierMeta, IDisplayableComponent
   {
      
      private static const WIDTH:int = 292;
      
      private static const HEIGHT:int = 283;
      
      private static const NORMAL_Y:Number = 365;
      
      private static const SMALL_Y:Number = 186;
      
      private static const HEIGHT_BREAKPOINT:Number = 960;
       
      
      private var _localVisibility:Boolean = true;
      
      private var _globalVisibility:Boolean = true;
      
      public function BattleNotifier()
      {
         super();
         setManageSize(true);
         setSize(WIDTH,HEIGHT);
         mouseChildren = false;
         mouseEnabled = false;
      }
      
      public function as_updateVisibility(param1:Boolean) : void
      {
         this._localVisibility = param1;
         this.updateVisibility();
      }
      
      public function isCompVisible() : Boolean
      {
         return visible;
      }
      
      public function setCompVisible(param1:Boolean) : void
      {
         this._globalVisibility = param1;
         this.updateVisibility();
      }
      
      public function updateStage(param1:Number, param2:Number) : void
      {
         if(_baseDisposed)
         {
            return;
         }
         y = param2 > HEIGHT_BREAKPOINT ? Number(NORMAL_Y) : Number(SMALL_Y);
      }
      
      private function updateVisibility() : void
      {
         visible = this._localVisibility && this._globalVisibility;
      }
   }
}
