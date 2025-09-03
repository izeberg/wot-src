package net.wg.gui.components.hintPanel
{
   import flash.display.BlendMode;
   import flash.display.Sprite;
   import flash.utils.getDefinitionByName;
   import net.wg.data.constants.Linkages;
   import net.wg.gui.battle.windows.vo.IngameDetailsKeyVO;
   import net.wg.gui.components.controls.Image;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class KeyViewersList extends Sprite implements IDisposable
   {
      
      private static const DEFAULT_KEY_GAP:int = 35;
      
      private static const PLUS_SIZE:int = 8;
       
      
      private var _keys:Vector.<KeyViewer>;
      
      private var _pluses:Vector.<Image>;
      
      private var _keyClass:Class = null;
      
      private var _keyGap:int = 35;
      
      private var _keySideOffset:int = 17;
      
      private var _disposed:Boolean = false;
      
      public function KeyViewersList()
      {
         this._keys = new Vector.<KeyViewer>(0);
         this._pluses = new Vector.<Image>(0);
         super();
         this._keyClass = getDefinitionByName(Linkages.KEY_VIEWER) as Class;
      }
      
      public function clearKeys() : void
      {
         var _loc1_:KeyViewer = null;
         var _loc2_:Image = null;
         for each(_loc1_ in this._keys)
         {
            removeChild(_loc1_);
            _loc1_.dispose();
            _loc1_ = null;
         }
         this._keys.splice(0,this._keys.length);
         for each(_loc2_ in this._pluses)
         {
            removeChild(_loc2_);
            _loc2_.dispose();
            _loc2_ = null;
         }
         this._pluses.splice(0,this._pluses.length);
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this.clearKeys();
         this._keys = null;
         this._pluses = null;
         this._keyClass = null;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function setKeys(param1:Vector.<IngameDetailsKeyVO>) : void
      {
         var _loc3_:Number = NaN;
         var _loc4_:Boolean = false;
         var _loc5_:IngameDetailsKeyVO = null;
         var _loc6_:KeyViewer = null;
         var _loc7_:Image = null;
         this.clearKeys();
         var _loc2_:int = param1.length;
         if(_loc2_ > 0)
         {
            _loc3_ = 0;
            _loc4_ = true;
            for each(_loc5_ in param1)
            {
               _loc6_ = new this._keyClass();
               _loc6_.keySideOffset = this._keySideOffset;
               _loc6_.setKey(_loc5_);
               _loc6_.x = _loc3_ >> 0;
               _loc3_ += _loc6_.width + this._keyGap;
               if(!_loc4_)
               {
                  _loc7_ = new Image();
                  _loc7_.source = RES_ICONS.MAPS_ICONS_LIBRARY_HINT_PLUS;
                  _loc7_.x = _loc6_.x - (this._keyGap + PLUS_SIZE >> 1);
                  _loc7_.y = _loc6_.height - PLUS_SIZE >> 1;
                  this._pluses.push(_loc7_);
                  addChild(_loc7_);
               }
               _loc4_ = false;
               this._keys.push(_loc6_);
               addChild(_loc6_);
            }
            cacheAsBitmap = true;
            blendMode = BlendMode.SCREEN;
         }
      }
      
      public function set keyClass(param1:Class) : void
      {
         if(param1 != null)
         {
            this._keyClass = param1;
         }
      }
      
      public function set keyGap(param1:int) : void
      {
         this._keyGap = param1;
      }
      
      public function set keySideOffset(param1:int) : void
      {
         this._keySideOffset = param1;
      }
   }
}
