package net.wg.gui.components.battleDamagePanel.components
{
   import flash.display.DisplayObjectContainer;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import flash.text.TextFormat;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.data.constants.generated.BATTLEDAMAGELOG_IMAGES;
   import net.wg.data.constants.generated.DAMAGE_LOG_SHELL_BG_TYPES;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import net.wg.infrastructure.managers.IAtlasManager;
   
   public class DamageLogRenderer extends MovieClip implements IDisposable
   {
      
      private static var _shellTFMaxWidth:int = -1;
      
      private static const ACTION_TYPE_X_POS:int = 49;
      
      private static const ACTION_ICON_Y_POS:int = 11;
      
      private static const VEH_ICON_Y_POS:int = 19;
      
      private static const SHELL_TEXT_PADDING:int = 8;
      
      private static const SHELL_BG_Y_POS:int = 12;
      
      private static const SHELL_TYPE_X_POS:int = 75;
      
      private static const SHELL_TF_X_OFFSET:int = 2;
      
      private static const SHELL_RIGHT_PADDING:int = 9;
      
      private static const SHELL_RIGHT_PADDING_EXTRA:int = 4;
      
      private static const VEH_TF_X_OFFSET:int = 10;
      
      private static const SHELL_TF_BORDER_PADDING:int = 2;
      
      private static const SHELL_MODE_ICON_Y_POS:int = 11;
      
      private static const COLOR_SHELL_TF_BLACK:uint = 0;
      
      private static const COLOR_SHELL_TF_WHITE:uint = 16777215;
      
      private static const COLOR_SHELL_TF_GOLD:uint = 16761699;
      
      private static const NAME_BG_IMG:String = "bgImg";
      
      private static const NAME_SHELL_TYPE_BG:String = "_shellTypeBG";
      
      private static const NAME_VEH_TYPE_IMG:String = "_vehTypeImg";
      
      private static const NAME_ACTION_TYPE_IMG:String = "_actionTypeImg";
      
      private static const NAME_SHELL_MODE_IMG:String = "_shellModeImg";
      
      private static const BLIND_POSTFIX:String = "Blind";
       
      
      public var valueTF:TextField;
      
      public var shellTypeTF:TextField;
      
      public var vehNameTF:TextField;
      
      private var _externalImagesContainer:DisplayObjectContainer = null;
      
      private var _actionTypeImg:Sprite = null;
      
      private var _shellModeImg:Sprite = null;
      
      private var _vehTypeImg:Sprite = null;
      
      private var _bgImg:Sprite = null;
      
      private var _shellTypeBG:ShellTypeBG = null;
      
      private var _atlasMgr:IAtlasManager;
      
      private var _atlasName:String = "";
      
      private var _actionAtlasIconPath:String = "";
      
      private var _isDisposed:Boolean = false;
      
      public function DamageLogRenderer()
      {
         this._atlasMgr = App.atlasMgr;
         super();
      }
      
      private static function getShellTfColorByType(param1:String) : uint
      {
         if(param1 == DAMAGE_LOG_SHELL_BG_TYPES.SPG)
         {
            return COLOR_SHELL_TF_WHITE;
         }
         if(param1 == DAMAGE_LOG_SHELL_BG_TYPES.SPG_HE_NO_STUN)
         {
            return COLOR_SHELL_TF_GOLD;
         }
         return COLOR_SHELL_TF_BLACK;
      }
      
      protected function onDispose() : void
      {
         this._externalImagesContainer.removeChild(this._actionTypeImg);
         this._actionTypeImg = null;
         this._externalImagesContainer.removeChild(this._shellTypeBG);
         this._shellTypeBG.dispose();
         this._shellTypeBG = null;
         this._externalImagesContainer.removeChild(this._shellModeImg);
         this._shellModeImg = null;
         this._externalImagesContainer.removeChild(this._vehTypeImg);
         this._vehTypeImg = null;
         this._externalImagesContainer.removeChild(this._bgImg);
         this._bgImg = null;
         this._externalImagesContainer = null;
         this._atlasMgr = null;
         this.shellTypeTF = null;
         this.valueTF = null;
         this.vehNameTF = null;
      }
      
      public final function dispose() : void
      {
         if(this._isDisposed)
         {
            return;
         }
         this.onDispose();
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function init(param1:DisplayObjectContainer, param2:Boolean, param3:Boolean, param4:String) : void
      {
         this._atlasName = param4;
         this._bgImg = new Sprite();
         this._bgImg.name = NAME_BG_IMG;
         this.valueTF.autoSize = TextFieldAutoSize.RIGHT;
         this.vehNameTF.autoSize = TextFieldAutoSize.LEFT;
         if(_shellTFMaxWidth <= 0)
         {
            this.calculateShellMaxWidth();
         }
         this.shellTypeTF.width = _shellTFMaxWidth + SHELL_TF_BORDER_PADDING;
         this._shellTypeBG = new ShellTypeBG(param4);
         this._shellTypeBG.name = NAME_SHELL_TYPE_BG;
         this._externalImagesContainer = param1;
         this._vehTypeImg = new Sprite();
         this._vehTypeImg.name = NAME_VEH_TYPE_IMG;
         this._actionTypeImg = new Sprite();
         this._actionTypeImg.name = NAME_ACTION_TYPE_IMG;
         this._actionTypeImg.y = ACTION_ICON_Y_POS;
         this._shellTypeBG.y = SHELL_BG_Y_POS;
         this._vehTypeImg.y = VEH_ICON_Y_POS;
         this._shellModeImg = new Sprite();
         this._shellModeImg.name = NAME_SHELL_MODE_IMG;
         this._shellModeImg.y = SHELL_MODE_ICON_Y_POS;
         param1.addChild(this._bgImg);
         param1.addChild(this._vehTypeImg);
         param1.addChild(this._actionTypeImg);
         param1.addChild(this._shellTypeBG);
         param1.addChild(this._shellModeImg);
         this.updateBG(param2,param3);
      }
      
      public function setData(param1:String, param2:String, param3:String, param4:String, param5:String, param6:String, param7:String, param8:Boolean, param9:Boolean) : void
      {
         this.valueTF.text = param1;
         this._actionAtlasIconPath = param2;
         this.setActionIcon(param8);
         this.shellTypeTF.text = param5;
         this._shellTypeBG.setData(param6);
         var _loc10_:uint = getShellTfColorByType(param6);
         var _loc11_:TextFormat = this.shellTypeTF.getTextFormat();
         if(_loc10_ != _loc11_.color)
         {
            _loc11_.color = _loc10_;
            this.shellTypeTF.setTextFormat(_loc11_);
         }
         if(param3 != Values.EMPTY_STR)
         {
            this._atlasMgr.drawGraphics(this._atlasName,param3,this._vehTypeImg.graphics,Values.EMPTY_STR,false,false,true);
            this.vehNameTF.text = param4;
         }
         if(param7)
         {
            this._atlasMgr.drawGraphics(this._atlasName,param7,this._shellModeImg.graphics);
         }
         this.updateItemsPositions(!param9);
      }
      
      public function updateBG(param1:Boolean, param2:Boolean) : void
      {
         var _loc3_:String = null;
         if(param1 && param2)
         {
            _loc3_ = BATTLEDAMAGELOG_IMAGES.DAMAGE_LOG_DETAIL_TOP;
         }
         else if(param2)
         {
            _loc3_ = BATTLEDAMAGELOG_IMAGES.DAMAGE_LOG_DETAIL_NO_BORDER;
         }
         else
         {
            _loc3_ = BATTLEDAMAGELOG_IMAGES.DAMAGELOG_DAMAGE_DETAIL;
         }
         this._atlasMgr.drawGraphics(this._atlasName,_loc3_,this._bgImg.graphics);
      }
      
      public function updateSettings(param1:Boolean) : void
      {
         this.setActionIcon(param1);
      }
      
      public function get externalImagesContainer() : DisplayObjectContainer
      {
         return this._externalImagesContainer;
      }
      
      private function updateItemsPositions(param1:Boolean) : void
      {
         var _loc2_:int = _shellTFMaxWidth + SHELL_TEXT_PADDING;
         if(param1)
         {
            this._shellTypeBG.updateWidth(_loc2_);
            this._shellTypeBG.x = SHELL_TYPE_X_POS;
            this.shellTypeTF.x = SHELL_TYPE_X_POS + SHELL_TF_X_OFFSET;
            this._shellModeImg.x = SHELL_TYPE_X_POS + _loc2_;
         }
         this.shellTypeTF.visible = this._shellTypeBG.visible = this._shellModeImg.visible = param1;
         this._actionTypeImg.x = ACTION_TYPE_X_POS;
         var _loc3_:int = !!param1 ? int(this._shellModeImg.x + SHELL_RIGHT_PADDING + (this._shellModeImg.width > 0 ? this._shellModeImg.width : SHELL_RIGHT_PADDING_EXTRA)) : int(SHELL_TYPE_X_POS + SHELL_TF_X_OFFSET);
         this._vehTypeImg.x = _loc3_;
         this.vehNameTF.x = _loc3_ + VEH_TF_X_OFFSET;
      }
      
      private function setActionIcon(param1:Boolean) : void
      {
         if(this._actionAtlasIconPath == Values.EMPTY_STR)
         {
            return;
         }
         var _loc2_:String = this._actionAtlasIconPath;
         if(param1 && BATTLEATLAS.DAMAGE_LOG_ALL_16X16_BLIND_ENUM.indexOf(_loc2_ + BLIND_POSTFIX) >= 0)
         {
            _loc2_ += BLIND_POSTFIX;
         }
         this._atlasMgr.drawGraphics(this._atlasName,_loc2_,this._actionTypeImg.graphics);
      }
      
      private function calculateShellMaxWidth() : void
      {
         var _loc1_:Vector.<String> = null;
         _loc1_ = new <String>[INGAME_GUI.DAMAGELOG_SHELLTYPE_ARMOR_PIERCING,INGAME_GUI.DAMAGELOG_SHELLTYPE_HIGH_EXPLOSIVE,INGAME_GUI.DAMAGELOG_SHELLTYPE_ARMOR_PIERCING_HE,INGAME_GUI.DAMAGELOG_SHELLTYPE_ARMOR_PIERCING_CR,INGAME_GUI.DAMAGELOG_SHELLTYPE_HOLLOW_CHARGE];
         var _loc2_:int = _loc1_.length;
         var _loc3_:int = 0;
         while(_loc3_ < _loc2_)
         {
            this.shellTypeTF.text = _loc1_[_loc3_];
            _shellTFMaxWidth = Math.max(_shellTFMaxWidth,this.shellTypeTF.textWidth);
            _loc3_++;
         }
      }
   }
}
