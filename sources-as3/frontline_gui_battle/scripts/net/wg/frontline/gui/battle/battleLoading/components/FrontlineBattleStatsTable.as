package net.wg.frontline.gui.battle.battleLoading.components
{
   import flash.display.MovieClip;
   import net.wg.gui.components.controls.ScrollBar;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class FrontlineBattleStatsTable extends MovieClip implements IDisposable
   {
       
      
      public var team1PlayerList:FrontlineBattleScrollingList = null;
      
      public var team2PlayerList:FrontlineBattleScrollingList = null;
      
      public var team1ScrollBar:ScrollBar = null;
      
      public var team2ScrollBar:ScrollBar = null;
      
      private var _disposed:Boolean = false;
      
      public function FrontlineBattleStatsTable()
      {
         super();
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this.onDispose();
      }
      
      protected function onDispose() : void
      {
         this.team1PlayerList.dispose();
         this.team1PlayerList = null;
         this.team2PlayerList.dispose();
         this.team2PlayerList = null;
         this.team1ScrollBar.dispose();
         this.team1ScrollBar = null;
         this.team2ScrollBar.dispose();
         this.team2ScrollBar = null;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
   }
}
