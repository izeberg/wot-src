package net.wg.gui.components.containers
{
   import flash.display.DisplayObject;
   import flash.events.Event;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import net.wg.data.constants.Errors;
   import net.wg.data.constants.generated.LAYER_NAMES;
   import net.wg.infrastructure.interfaces.IInnerView;
   import net.wg.infrastructure.interfaces.ILobbyPageSubContainer;
   import net.wg.infrastructure.interfaces.IManagedContent;
   import net.wg.infrastructure.interfaces.IView;
   import net.wg.utils.IAssertable;
   import net.wg.utils.StaticUtils;
   
   public class LobbyPageSubContainer extends ManagedContainer implements ILobbyPageSubContainer
   {
      
      public static const FRAMED_MODE_CHANGED:String = "framedModeChanged";
       
      
      private var _pagePadding:Rectangle;
      
      private var _innerPadding:Rectangle;
      
      private var _innerSize:Point;
      
      private var _pageSize:Point;
      
      private var _asserter:IAssertable;
      
      private var _fullscreenMode:Boolean = true;
      
      private var _framedViews:Vector.<IManagedContent>;
      
      private var _hasFramedViews:Boolean = false;
      
      private var _framedState:Boolean = false;
      
      public function LobbyPageSubContainer(param1:String)
      {
         this._pagePadding = new Rectangle();
         this._innerPadding = new Rectangle();
         this._innerSize = new Point();
         this._pageSize = new Point();
         super(param1);
         this._asserter = App.utils.asserter;
         this._framedViews = new Vector.<IManagedContent>();
      }
      
      override public function canFocusNextLayer(param1:String) : Boolean
      {
         if(param1 == LAYER_NAMES.VIEWS)
         {
            return true;
         }
         return super.canFocusNextLayer(param1);
      }
      
      override public function updateStage(param1:Number, param2:Number, param3:Rectangle = null) : void
      {
         if(this._pageSize.x == param1 && this._pageSize.y == param2 && this._pagePadding.x == param3.x && this._pagePadding.y == param3.y && this._pagePadding.width == param3.width && this._pagePadding.height == param3.height && this._framedState == this._hasFramedViews)
         {
            return;
         }
         this._pageSize.x = param1;
         this._pageSize.y = param2;
         this._pagePadding = param3;
         this._framedState = this._hasFramedViews;
         if(this._fullscreenMode && !this._hasFramedViews)
         {
            x = 0;
            y = 0;
            this._innerSize.x = param1;
            this._innerSize.y = param2;
            this._innerPadding = param3;
            super.updateStage(param1,param2);
         }
         else
         {
            x = param3.x;
            y = param3.y;
            this._innerSize.x = param1 - param3.x - param3.width;
            this._innerSize.y = param2 - param3.y - param3.height;
            this._innerPadding = new Rectangle();
            super.updateStage(this._innerSize.x,this._innerSize.y);
         }
      }
      
      override protected function viewUpdateStage(param1:DisplayObject) : void
      {
         var _loc3_:IView = null;
         var _loc2_:IInnerView = param1 as IInnerView;
         if(_loc2_ && _loc2_.isFullScreenModeSupported())
         {
            param1.x = 0;
            param1.y = 0;
            _loc2_.updateStageWithPadding(this._innerSize.x,this._innerSize.y,new Rectangle(this._innerPadding.x,this._innerPadding.y,this._innerPadding.width,this._innerPadding.height));
            return;
         }
         if(param1 is IView)
         {
            _loc3_ = IView(param1);
            _loc3_.x = this._innerPadding.x;
            _loc3_.y = this._innerPadding.y;
            _loc3_.updateStage(this._innerSize.x,this._innerSize.y);
            return;
         }
         super.viewUpdateStage(param1);
      }
      
      override protected function onDispose() : void
      {
         this._asserter = null;
         this._framedViews.splice(0,this._framedViews.length);
         this._framedViews = null;
         this._pagePadding = null;
         this._innerPadding = null;
         this._pageSize = null;
         this._innerSize = null;
         super.onDispose();
      }
      
      override protected function onViewVisibilityChanged(param1:IManagedContent, param2:Boolean) : void
      {
         var _loc5_:Number = NaN;
         var _loc3_:IInnerView = param1 as IInnerView;
         if(_loc3_ && _loc3_.isFullScreenModeSupported())
         {
            return;
         }
         var _loc4_:String = StaticUtils.getObjectHierarchy(param1 as DisplayObject,this);
         if(param2)
         {
            this._asserter.assert(this._framedViews.indexOf(param1) == -1,_loc4_ + Errors.ALREADY_REGISTERED);
            this._framedViews.push(param1);
         }
         else
         {
            _loc5_ = this._framedViews.indexOf(param1);
            this._asserter.assert(_loc5_ != -1,_loc4_ + Errors.WASNT_FOUND);
            this._framedViews.splice(_loc5_,1);
            this._asserter.assert(this._framedViews.indexOf(param1) == -1,_loc4_ + Errors.WASNT_UNREGISTERED);
         }
         this.setFramedViews(this._framedViews.length > 0);
      }
      
      public function setFramedViews(param1:Boolean) : void
      {
         if(this._hasFramedViews == param1)
         {
            return;
         }
         this._hasFramedViews = param1;
         this.updateStage(this._pageSize.x,this._pageSize.y,this._pagePadding);
         dispatchEvent(new Event(FRAMED_MODE_CHANGED));
      }
      
      override public function get paddings() : Rectangle
      {
         return this._pagePadding;
      }
      
      public function get isFramedMode() : Boolean
      {
         return this._hasFramedViews;
      }
   }
}
