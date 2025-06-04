package net.wg.gui.messenger.controls
{
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import net.wg.data.constants.generated.TOOLTIPS_CONSTANTS;
   import net.wg.gui.messenger.data.ContactItemVO;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import scaleform.clik.core.UIComponent;
   import scaleform.clik.events.InputEvent;
   
   public class ContactsListItemRenderer extends ContactItemRenderer
   {
      
      private static const UPDATE_DATA:String = "updD";
       
      
      public var hit:Sprite;
      
      private var _contactItem:ContactItem;
      
      private var _myData:ContactItemVO;
      
      private var _toolTipMgr:ITooltipMgr;
      
      public function ContactsListItemRenderer()
      {
         this._toolTipMgr = App.toolTipMgr;
         constraintsDisabled = true;
         this.hitArea = this.hit;
         super();
      }
      
      override public function getCurrentContentItem() : UIComponent
      {
         return this._contactItem;
      }
      
      override public function getData() : Object
      {
         return this._myData;
      }
      
      override public function setData(param1:Object) : void
      {
         this._myData = Boolean(param1) ? (param1 is ContactItemVO ? ContactItemVO(param1) : new ContactItemVO(param1)) : null;
         invalidate(UPDATE_DATA);
      }
      
      override protected function preInitialize() : void
      {
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(UPDATE_DATA))
         {
            if(this._myData)
            {
               visible = true;
               if(!this._contactItem)
               {
                  this._contactItem = App.utils.classFactory.getComponent("ContactItemUI",ContactItem);
                  this._contactItem.width = _width / scaleX;
                  this._contactItem.height = _height / scaleY;
                  this._contactItem.validateNow();
                  addChild(this._contactItem);
               }
               this._contactItem.update(this._myData);
               this._contactItem.validateNow();
            }
            else
            {
               visible = false;
            }
         }
         if(isInvalid(UPDATE_DATA) || isInvalid(DRAGGING_ITEM_INV))
         {
            alpha = !isNaN(draggedItemId) && this._contactItem != null && ContactItemVO(this._contactItem.data).dbID == draggedItemId ? Number(0.3) : Number(1);
         }
      }
      
      override protected function onDispose() : void
      {
         if(this._contactItem)
         {
            this._contactItem.dispose();
            this._contactItem = null;
         }
         this._myData = null;
         this.hit = null;
         this._toolTipMgr = null;
         super.onDispose();
      }
      
      [Inspectable(defaultValue="",type="string")]
      override public function get data() : Object
      {
         return this._myData;
      }
      
      override public function handleInput(param1:InputEvent) : void
      {
      }
      
      override protected function handleMouseRollOver(param1:MouseEvent) : void
      {
         var _loc2_:ContactItemVO = null;
         super.handleMouseRollOver(param1);
         if(this._contactItem && this._myData)
         {
            _loc2_ = ContactItemVO(this._contactItem.data);
            this._toolTipMgr.showSpecial(TOOLTIPS_CONSTANTS.CONTACT,null,_loc2_.dbID,App.utils.commons.getFullPlayerName(_loc2_.userPropsVO));
         }
      }
      
      override protected function handleMouseRollOut(param1:MouseEvent) : void
      {
         super.handleMouseRollOut(param1);
         this._toolTipMgr.hide();
      }
   }
}
