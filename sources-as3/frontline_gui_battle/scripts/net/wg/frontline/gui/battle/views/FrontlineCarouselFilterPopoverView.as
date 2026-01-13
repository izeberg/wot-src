package net.wg.frontline.gui.battle.views
{
   import flash.text.TextField;
   import net.wg.frontline.gui.battle.components.FrontlineFilterDropDown;
   import net.wg.frontline.gui.battle.views.data.PlayListsVO;
   import net.wg.frontline.infrastructure.base.meta.impl.FrontlineCarouselFilterPopoverMeta;
   import net.wg.gui.components.controls.ResizableScrollPane;
   import net.wg.gui.components.controls.ScrollBar;
   import net.wg.gui.components.popovers.PopOverConst;
   import scaleform.clik.events.ListEvent;
   
   public class FrontlineCarouselFilterPopoverView extends FrontlineCarouselFilterPopoverMeta
   {
      
      protected static const NOTE_OFFSET:int = -2;
      
      protected static const SEPARATOR_OFFSET:int = -23;
      
      protected static const SEARCH_INPUT_OFFSET:int = 9;
      
      private static const SCROLL_STEP_FACTOR:int = 30;
      
      private static const SCROLL_PANE_MAX_HEIGHT:uint = 391;
       
      
      public var playLists:FrontlineFilterDropDown = null;
      
      public var scrollBar:ScrollBar = null;
      
      public var scrollPane:ResizableScrollPane = null;
      
      public var note:TextField = null;
      
      public function FrontlineCarouselFilterPopoverView()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.playLists.addEventListener(ListEvent.INDEX_CHANGE,this.onPlayListsIndexChangeHandler);
         this.scrollPane.scrollBar = this.scrollBar;
         this.scrollPane.scrollStepFactor = SCROLL_STEP_FACTOR;
         this.scrollPane.target = content;
         this.scrollPane.scrollPosition = 0;
         this.note.text = FL_COMMON.FILTERPOPOVER_NOTE;
      }
      
      override protected function draw() : void
      {
         super.draw();
      }
      
      override protected function onDispose() : void
      {
         this.playLists.removeEventListener(ListEvent.INDEX_CHANGE,this.onPlayListsIndexChangeHandler);
         this.playLists.dispose();
         this.playLists = null;
         this.scrollPane.target = null;
         this.scrollPane.dispose();
         this.scrollPane = null;
         this.scrollBar = null;
         this.note = null;
         super.onDispose();
      }
      
      override protected function getNewHeight(param1:int) : int
      {
         if(initData.searchSectionVisible)
         {
            this.note.y = param1 + NOTE_OFFSET;
            separatorBottom.y = this.note.y + this.note.textHeight + SEPARATOR_OFFSET | 0;
            searchInput.y = separatorBottom.y + separatorBottom.height + SEARCH_INPUT_OFFSET | 0;
            param1 = searchInput.y + searchInput.height + PADDING;
         }
         return param1;
      }
      
      override protected function getPreferredLayout() : int
      {
         return PopOverConst.ARROW_BOTTOM;
      }
      
      override protected function updateSize() : void
      {
         this.scrollPane.setSize(width,Math.min(content.height,SCROLL_PANE_MAX_HEIGHT));
         this.scrollBar.height = this.scrollPane.height;
         setViewSize(width,this.getNewHeight(this.scrollPane.y + this.scrollPane.height));
      }
      
      override protected function updatePlayLists(param1:PlayListsVO) : void
      {
         this.playLists.dataProvider = param1.lists;
         this.playLists.selectedIndex = param1.selectedListIndex;
      }
      
      private function onPlayListsIndexChangeHandler(param1:ListEvent) : void
      {
         onPlayListsChangeS(param1.itemData.id);
      }
   }
}
