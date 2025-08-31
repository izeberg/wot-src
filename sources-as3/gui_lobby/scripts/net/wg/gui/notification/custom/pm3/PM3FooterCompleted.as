package net.wg.gui.notification.custom.pm3
{
   import flash.display.Sprite;
   import net.wg.data.constants.Linkages;
   import net.wg.gui.components.controls.SimpleTileList;
   import net.wg.infrastructure.interfaces.IDisposableSprite;
   import scaleform.clik.constants.DirectionMode;
   import scaleform.clik.data.DataProvider;
   
   public class PM3FooterCompleted extends Sprite implements IDisposableSprite
   {
      
      private static const RENDERER_WIDTH:int = 48;
      
      private static const RENDERER_HEIGHT:int = 48;
      
      private static const AVAILABLE_WIDTH:int = 288;
       
      
      public var missionsList:SimpleTileList;
      
      private var _isDisposed:Boolean = false;
      
      public function PM3FooterCompleted()
      {
         super();
      }
      
      public final function dispose() : void
      {
         this.missionsList.dispose();
         this.missionsList = null;
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function setData(param1:DataProvider) : void
      {
         if(param1 == null)
         {
            return;
         }
         this.missionsList.itemRenderer = App.utils.classFactory.getClass(Linkages.AWARD_RENDERER);
         this.missionsList.directionMode = DirectionMode.HORIZONTAL;
         this.missionsList.tileWidth = RENDERER_WIDTH;
         this.missionsList.tileHeight = RENDERER_HEIGHT;
         this.missionsList.renderersAlign = SimpleTileList.RENDERERS_ALIGN_CENTER;
         this.missionsList.dataProvider = param1;
         this.missionsList.horizontalGap = 10;
         this.missionsList.verticalGap = 10;
         this.missionsList.width = AVAILABLE_WIDTH;
         this.missionsList.validateNow();
         this.missionsList.setRenderersSize(RENDERER_WIDTH,RENDERER_HEIGHT);
      }
      
      override public function get height() : Number
      {
         return this.missionsList.y + this.missionsList.height;
      }
   }
}
