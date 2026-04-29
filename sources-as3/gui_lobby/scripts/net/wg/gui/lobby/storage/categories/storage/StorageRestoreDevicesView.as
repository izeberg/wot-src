package net.wg.gui.lobby.storage.categories.storage
{
   import flash.display.Graphics;
   import flash.display.Sprite;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.data.constants.generated.STORAGE_CONSTANTS;
   import net.wg.gui.components.advanced.interfaces.IBackButton;
   import net.wg.gui.lobby.storage.data.StorageRestoreDevicesVO;
   import net.wg.infrastructure.base.meta.IStorageRestoreDevicesViewMeta;
   import net.wg.infrastructure.base.meta.impl.StorageRestoreDevicesViewMeta;
   import net.wg.utils.IStageSizeDependComponent;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   
   public class StorageRestoreDevicesView extends StorageRestoreDevicesViewMeta implements IStorageRestoreDevicesViewMeta, IStageSizeDependComponent
   {
      
      private static const HIT_AREA_NAME:String = "hitArea";
      
      private static const SMALL_CONTENT_Y_OFFSET:int = 10;
      
      private static const NORMAL_CONTENT_Y_OFFSET:int = 35;
      
      private static const SMALL_TITLE_Y_OFFSET:int = 65;
      
      private static const NORMAL_TITLE_Y_OFFSET:int = 90;
      
      private static const BACK_BUTTON_Y_OFFSET:int = 2;
      
      private static const BACK_BUTTON_MIN_X_VALUE:int = 185;
       
      
      public var title:TextField = null;
      
      public var content:StorageRestoreDevicesContent = null;
      
      public var backButton:IBackButton = null;
      
      private var _hitArea:Sprite = null;
      
      public function StorageRestoreDevicesView()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.title.autoSize = TextFieldAutoSize.LEFT;
         this.title.mouseWheelEnabled = this.title.mouseEnabled = false;
         this._hitArea = new Sprite();
         this._hitArea.name = HIT_AREA_NAME;
         addChildAt(this._hitArea,0);
         this.content.setHitArea(this._hitArea);
         this.content.invalidateLayout();
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         this.backButton.addEventListener(ButtonEvent.CLICK,this.onBackBtnClickHandler);
         registerFlashComponentS(this.content,STORAGE_CONSTANTS.STORAGE_RESTORE_DEVICES_CONTENT);
         this.content.setActive(true);
         App.stageSizeMgr.register(this);
         this.updateStage(width,height);
      }
      
      override protected function onDispose() : void
      {
         App.stageSizeMgr.unregister(this);
         this.backButton.removeEventListener(ButtonEvent.CLICK,this.onBackBtnClickHandler);
         this.backButton.dispose();
         this.backButton = null;
         this.title = null;
         this.content = null;
         this._hitArea.graphics.clear();
         this._hitArea = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this.content && isInvalid(InvalidationType.SIZE))
         {
            this.title.x = width - this.content.contentWidth >> 1;
            this.backButton.descrVisible = this.title.x > BACK_BUTTON_MIN_X_VALUE;
         }
      }
      
      override protected function setData(param1:StorageRestoreDevicesVO) : void
      {
         this.backButton.label = param1.backBtn;
         this.backButton.descrLabel = param1.backBtnLabel;
         this.title.text = param1.titleLabel;
         setBackground(param1.bgSource);
      }
      
      override protected function onEscapeKeyDown() : void
      {
         onBackClickS();
      }
      
      private function onBackBtnClickHandler(param1:ButtonEvent) : void
      {
         onBackClickS();
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         setSize(param1,param2);
         this.content.setSize(param1 - this.content.x,param2 - this.content.y);
         var _loc3_:Graphics = this._hitArea.graphics;
         _loc3_.clear();
         _loc3_.beginFill(16711680,0);
         _loc3_.drawRect(0,0,param1,param2);
      }
      
      public function setStateSizeBoundaries(param1:int, param2:int) : void
      {
         if(param2 <= StageSizeBoundaries.HEIGHT_768)
         {
            this.content.y = SMALL_CONTENT_Y_OFFSET;
            this.title.y = SMALL_TITLE_Y_OFFSET;
         }
         else
         {
            this.content.y = NORMAL_CONTENT_Y_OFFSET;
            this.title.y = NORMAL_TITLE_Y_OFFSET;
         }
         this.backButton.y = this.title.y + BACK_BUTTON_Y_OFFSET;
      }
   }
}
