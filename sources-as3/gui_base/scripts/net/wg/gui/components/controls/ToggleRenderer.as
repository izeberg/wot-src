package net.wg.gui.components.controls
{
   import flash.text.TextFormatAlign;
   import net.wg.data.constants.Linkages;
   import net.wg.gui.components.common.counters.Counter;
   import net.wg.gui.components.controls.VO.SimpleRendererVO;
   import net.wg.gui.components.controls.events.RendererEvent;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.managers.counter.CounterProps;
   import net.wg.utils.ICounterManager;
   import net.wg.utils.ICounterProps;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.core.UIComponent;
   import scaleform.clik.data.ListData;
   import scaleform.clik.events.ButtonEvent;
   import scaleform.clik.interfaces.IListItemRenderer;
   
   public class ToggleRenderer extends UIComponentEx implements IListItemRenderer
   {
      
      public static const COUNTER_DEFAULT_OFFSET_X:int = 3;
      
      public static const COUNTER_DEFAULT_OFFSET_Y:int = 1;
      
      public static const COUNTER_TF_PADDING:int = 0;
       
      
      public var btn:BlackButton = null;
      
      private var _rendererData:SimpleRendererVO = null;
      
      private var _index:uint = 0;
      
      private var _selected:Boolean = false;
      
      private var _updateSelectedFromData:Boolean = true;
      
      private var _counterManager:ICounterManager;
      
      public function ToggleRenderer()
      {
         this._counterManager = App.utils.counterManager;
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.btn.toggleEnable = true;
         this.btn.addEventListener(ButtonEvent.CLICK,this.onBtnClickHandler);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            if(this._rendererData != null)
            {
               this.btn.visible = true;
               this.btn.iconSource = this._rendererData.value;
               if(this._updateSelectedFromData)
               {
                  this.btn.selected = this._rendererData.selected;
               }
               this.btn.tooltip = this._rendererData.tooltip;
               this.btn.enabled = this._rendererData.enabled;
               this.updateCounter(this._rendererData.isNew);
            }
            else
            {
               this.btn.visible = false;
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this._counterManager.disposeCountersForContainer(this.getCounterContainerUIID());
         this._counterManager = null;
         this.btn.removeEventListener(ButtonEvent.CLICK,this.onBtnClickHandler);
         this.btn.dispose();
         this.btn = null;
         this._rendererData = null;
         super.onDispose();
      }
      
      public function getData() : Object
      {
         return this._rendererData;
      }
      
      public function setData(param1:Object) : void
      {
         if(param1 != null)
         {
            this._rendererData = SimpleRendererVO(param1);
         }
         else
         {
            this._rendererData = null;
         }
         invalidateData();
      }
      
      public function setListData(param1:ListData) : void
      {
         this.index = param1.index;
         this.selected = param1.selected;
      }
      
      public function set updateSelectedFromData(param1:Boolean) : void
      {
         this._updateSelectedFromData = param1;
      }
      
      public function get index() : uint
      {
         return this._index;
      }
      
      public function set index(param1:uint) : void
      {
         this._index = param1;
      }
      
      public function get selectable() : Boolean
      {
         return this.btn.selected;
      }
      
      public function set selectable(param1:Boolean) : void
      {
         this._rendererData.selected = param1;
         this.btn.selected = param1;
      }
      
      public function get owner() : UIComponent
      {
         return this.btn.owner;
      }
      
      public function set owner(param1:UIComponent) : void
      {
         this.btn.owner = param1;
      }
      
      public function get selected() : Boolean
      {
         return this._selected;
      }
      
      public function set selected(param1:Boolean) : void
      {
         this._selected = param1;
      }
      
      private function onBtnClickHandler(param1:ButtonEvent) : void
      {
         this.selectable = !this.selectable;
         dispatchEvent(new RendererEvent(RendererEvent.ITEM_CLICK,this._index,true));
      }
      
      private function updateCounter(param1:Boolean) : void
      {
         if(param1)
         {
            this._counterManager.setCounter(this.btn,"",this.getCounterContainerUIID(),this.getCounterProps());
         }
         else
         {
            this._counterManager.removeCounter(this.btn,this.getCounterContainerUIID());
         }
      }
      
      private function getCounterContainerUIID() : String
      {
         return this.name;
      }
      
      private function getCounterProps() : ICounterProps
      {
         return new CounterProps(COUNTER_DEFAULT_OFFSET_X,COUNTER_DEFAULT_OFFSET_Y,TextFormatAlign.RIGHT,true,Linkages.COUNTER_UI,COUNTER_TF_PADDING,false,Counter.EMPTY_STATE);
      }
   }
}
