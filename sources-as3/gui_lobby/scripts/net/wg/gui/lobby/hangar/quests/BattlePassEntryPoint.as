package net.wg.gui.lobby.hangar.quests
{
   import flash.events.Event;
   import net.wg.infrastructure.base.meta.IBattlePassEntryPointMeta;
   import net.wg.infrastructure.base.meta.impl.BattlePassEntryPointMeta;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.constants.InvalidationType;
   
   public class BattlePassEntryPoint extends BattlePassEntryPointMeta implements IBattlePassEntryPointMeta
   {
      
      private static const BP_ENTRY_POINT_OUTER_MARGIN_X:int = -56;
      
      private static const BP_ENTRY_POINT_OUTER_MARGIN_SMALL_X:int = -83;
      
      private static const SIZE:int = 256;
      
      private static const SIZE_SMALL:int = 255;
      
      private static const VISIBLE_SIZE_HEIGHT:int = 135;
      
      private static const VISIBLE_SMALL_SIZE_HEIGHT:int = 105;
      
      private static const VISIBLE_SMALL_SIZE_CHOSEN_HEIGHT:int = 117;
      
      private static const VISIBLE_SIZE_CHOSEN_HEIGHT:int = 153;
       
      
      private var _isSmall:Boolean = false;
      
      private var _isChapterChosen:Boolean = false;
      
      public function BattlePassEntryPoint()
      {
         super();
         setManageSize(true);
         setSize(SIZE,SIZE);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         x = -(SIZE >> 1);
         App.stage.addEventListener(Event.RESIZE,this.onStageResizeHandler,false,0,true);
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         setIsSmallS(this._isSmall);
         var _loc1_:int = !!this._isSmall ? int(SIZE_SMALL) : int(SIZE);
         setSize(_loc1_,_loc1_);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            if(App.stage.stageWidth >= StageSizeBoundaries.WIDTH_1600 && App.stage.stageHeight >= StageSizeBoundaries.HEIGHT_900)
            {
               this.setIsSmallSize(false);
            }
            else
            {
               this.setIsSmallSize(true);
            }
            dispatchEvent(new Event(Event.RESIZE));
         }
      }
      
      override protected function onDispose() : void
      {
         App.stage.removeEventListener(Event.RESIZE,this.onStageResizeHandler);
         super.onDispose();
      }
      
      public function as_isChapterChosen(param1:Boolean) : void
      {
         this._isChapterChosen = param1;
         invalidateSize();
      }
      
      private function setIsSmallSize(param1:Boolean) : void
      {
         var _loc2_:int = 0;
         if(this._isSmall != param1)
         {
            this._isSmall = param1;
            if(!isDAAPIInited)
            {
               return;
            }
            setIsSmallS(this._isSmall);
            _loc2_ = !!this._isSmall ? int(SIZE_SMALL) : int(SIZE);
            setSize(_loc2_,_loc2_);
         }
      }
      
      override public function get marginRight() : int
      {
         return !!this._isSmall ? int(BP_ENTRY_POINT_OUTER_MARGIN_SMALL_X) : int(BP_ENTRY_POINT_OUTER_MARGIN_X);
      }
      
      override public function get marginLeft() : int
      {
         return !!this._isSmall ? int(BP_ENTRY_POINT_OUTER_MARGIN_SMALL_X) : int(BP_ENTRY_POINT_OUTER_MARGIN_X);
      }
      
      override public function get visibleHeight() : int
      {
         if(this._isChapterChosen)
         {
            return !!this._isSmall ? int(VISIBLE_SMALL_SIZE_CHOSEN_HEIGHT) : int(VISIBLE_SIZE_CHOSEN_HEIGHT);
         }
         return !!this._isSmall ? int(VISIBLE_SMALL_SIZE_HEIGHT) : int(VISIBLE_SIZE_HEIGHT);
      }
      
      private function onStageResizeHandler(param1:Event) : void
      {
         invalidateSize();
      }
   }
}
