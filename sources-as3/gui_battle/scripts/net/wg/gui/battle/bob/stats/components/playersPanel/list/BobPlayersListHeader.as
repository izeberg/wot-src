package net.wg.gui.battle.bob.stats.components.playersPanel.list
{
   import flash.display.Sprite;
   import flash.geom.ColorTransform;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class BobPlayersListHeader extends Sprite implements IDisposable
   {
      
      private static const BOB_PLAYERS_LIST_HEADER_SCHEME_PREFIX:String = "blogger_";
      
      private static const LABELS_PADDING:int = 33;
       
      
      public var headerLabels:BobPlayersListHeaderLabels;
      
      public var background:Sprite;
      
      private var _isRightAligned:Boolean;
      
      private var _disposed:Boolean = false;
      
      public function BobPlayersListHeader()
      {
         super();
      }
      
      public final function dispose() : void
      {
         this.headerLabels.dispose();
         this.headerLabels = null;
         this.background = null;
         this._disposed = true;
      }
      
      public final function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function setBloggerId(param1:int) : void
      {
         var _loc2_:ColorTransform = App.colorSchemeMgr.getTransform(BOB_PLAYERS_LIST_HEADER_SCHEME_PREFIX + param1);
         this.background.transform.colorTransform = _loc2_;
         this.headerLabels.setBloggerId(param1);
         this.updatePositions();
      }
      
      public function setIsRightAligned(param1:Boolean) : void
      {
         this._isRightAligned = param1;
         this.updatePositions();
      }
      
      private function updatePositions() : void
      {
         if(this._isRightAligned)
         {
            this.headerLabels.x = -this.headerLabels.width - LABELS_PADDING;
         }
         else
         {
            this.headerLabels.x = LABELS_PADDING;
         }
      }
   }
}
